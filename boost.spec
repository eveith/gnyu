Name: boost
Version: 1.34.1
Release: 1ev
Summary: A set of free, peer-reviewed, portable C++ source libraries
URL: http://www.boost.org/
Group: System Environment/Libraries
License: Boost Software License 1.0
Vendor: GNyU-Linux
Source: http://downloads.sourceforge.net/boost/boost_1_34_1.tar.bz2
Patch: %{name}-jam_src_build-gcc42.patch
Patch1: %{name}-use-rpm-optflags.patch
Patch2: %{name}-configure.patch
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc, python

%description


%prep
%setup -q -n boost_1_34_1
%patch -p0
%patch1 -p0
%patch2 -p0


%build
(cd tools/jam/src && ./build.sh)
export CFLAGS="${RPM_OPT_FLAGS}" CXXFLAGS="${RPM_OPT_FLAGS}"
./configure \
	--with-toolset=gcc \
	--prefix='%{_prefix}' \
	--with-icu
%{__make} %{?_smp_mflags} all


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__mkdir_p} %{buildroot}/{%{_libdir},%{_includedir}}

# It gets a little bit ugly here, because boost does not favour a build system
# that allows something like 'DESTDIR'.
%{__find} boost -type d \
	-exec %{__mkdir_p} '%{buildroot}/%{_includedir}/{}' \; \
	-print
%{__find} boost -type f \
	-exec %{__install} -p -m 0644 '{}' \
		'%{buildroot}/%{_includedir}/{}' \; \
	-print
pushd stage/lib
%{__find} . -type f \
	\( -name \*.a \
		-exec %{__install} -p -m 0644 '{}' \
			"%{buildroot}/%{_libdir}/$(basename {})" \; \
	\) -or \( -name \*.so \
		-exec %{__install} -p -m 0755 '{}' \
			"%{buildroot}/%{_libdir}/$(basename {}.%{version})" \; \
	\) -print
popd
pushd %{buildroot}/%{_libdir}
for lib in $(%{__find} . -type f -name \*.so -print)
do
	%{__ln_s} "{lib}" "${lib%%.*}.3"
done
popd
%{__find} %{buildroot}/%{_includedir} -type f \
	\( -name \*.pl -or -name \*.sh \) -exec %{__rm} -vf {} \;

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc doc/html README LICENSE*
%{_includedir}/boost/
%{_libdir}/libboost_*.a
%{_libdir}/libboost_*.so*

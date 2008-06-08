Name: ode
Version: 0.9
Release: 1ev
Summary: A physics SDK for simulating rigid body dynamics
URL: http://www.ode.org/
Group: System Environment/Libraries
License: BSD
Vendor: GNyU-Linux
Source: http://downloads.sourceforge.net/opende/ode-src-%{version}.zip
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: coreutils, grep, sed, make, gcc-g++, mesalib, libstdc++
BuildRequires: libgcc_s

%description


%prep
%setup -q


%build
%configure \
	--enable-double-precision \
	--with-trimesh=opcode \
	--enable-release-builds \
	--enable-shared
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'

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
%doc CHANGELOG.txt LICENSE-BSD.TXT LICENSE.TXT README.txt OPCODE
%{_bindir}/ode-config
%{_includedir}/ode/
%{_libdir}/libode.*

Name: initng
Version: 0.6.10.1
Release: 1ev
Summary: The next generation init system
URL: http://www.initng.org/
Group: System Environment/Base
License: GPL
Vendor: MSP Slackware
Source: http://download.initng.org/initng/v0.6/initng-%{version}.tar.bz2
Patch0: initng-fix_manpath.patch
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: cmake >= 2.2.0, make, gcc-core, dbus

%description
Initng is a full replacement of the old and in many ways deprecated sysvinit
tool. It is designed with speed in mind, doing as much as possible
asynchronously. In other words: It will boot your unix-system much faster, and
give you more control and statistics over your system.
The basic premise is that startup commands can be launched as soon as their
dependencies are met. This limits the effect of bottlenecks like I/O
operations;
while one program is performing I/O, another can be utilizing the processor.
Initng tracks the individual service dependencies in its configuration files.
It is designed to use a minimum of system resources and to boot your system
quickly and safely.


%prep
%setup -q 
%patch -P 0 -p1

# Remove doc files we install anyways.
sed -i 's,INSTALL_FILES(${DATA_INSTALL_DIR}/doc/initng FILES ${DOC_FILES}),,'\
	doc/CMakeLists.txt



%build
cmake \
	-DCMAKE_BUILD_TYPE:STRING=None \
	-DCMAKE_C_FLAGS:STRING="$RPM_OPT_FLAGS" \
	-DCMAKE_C_COMPILER=${CC:-"$(which %{_target_platform}-gcc)"} \
	-DDATA_INSTALL_DIR:STRING="%{_datadir}" \
	-DMAN_INSTALL_DIR:STRING="%{_mandir}" \
	-DINCLUDE_INSTALL_DIR:STRING="%{_includedir}" \
	-DLIB_INSTALL_DIR:STRING="/%{_lib}" \
	-DSBIN_INSTALL_DIR:STRING="/sbin" \
	-DSYSCONF_INSTALL_DIR:STRING="/etc" \
	-DBUILD_DAEMON_CLEAN=OFF \
	-DINSTALL_AS_INIT=ON \
	-DCOUNT_ME=OFF \
	.	
make %{_smp_mflags}


%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"

# Create some neccessary directories.

pushd "$RPM_BUILD_ROOT"
mkdir -p etc/initng/{runlevel,system,service,daemon}
popd


[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ] \
    && rm -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"


%post
/sbin/ldconfig
/sbin/ngc -c --quiet 2> /dev/null

%postun
/sbin/ldconfig


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README TODO doc/
/etc/initng/
/bin/pidof
/%{_lib}/libinitng*.so*
/%{_lib}/libng?client*.so*
/%{_lib}/initng/
/sbin/*
%{_includedir}/initng/
%{_mandir}/man8/initng.8*
%{_mandir}/man8/ng*c.8*

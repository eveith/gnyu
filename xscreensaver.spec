Name: xscreensaver
Version: 5.04
Release: 1ev
Summary: A collection of free screen savers for X11
URL: http://www.jwz.org/xscreensaver/
Group: User Interface/X
License: BSD, MIT
Vendor: MSP Slackware
Source0: http://www.jwz.org/%{name}/%{name}-%{version}.tar.gz
Source1: %{name}.pamd
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, libjpeg, libpng, libpam, mesalib, gtk2
BuildRequires: mesalib, libICE, libSM, libX11, libXext, libXinerama
BuildRequires: libXmu, libXpm, libXrandr, libXrender, libXt

%description
XScreenSaver is the standard screen saver collection shipped on most Linux and
Unix systems running the X11 Window System. These screen savers also work on
Mac OS (X11 is not required). More than 200 screen savers are included.


%prep
%setup -q


%build
%configure \
	--with-gl \
	--with-pixbuf \
	--with-jpeg \
	--with-xshm-ext \
	--with-xdbe-ext \
	--with-browser=%{_bindir}/konqueror \
	--with-gtk \
	--with-pam \
	--with-pam-service-name=xscreensaver \
	--with-randr-ext \
	--with-dpms-ext \
	--with-xinerama-ext \
	--with-proc-interrupts
make %{_smp_mflags}


%install
[ -d "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != '/' ] && rm -rf "$RPM_BUILD_ROOT"
make install install_prefix="$RPM_BUILD_ROOT"

%find_lang xscreensaver

# Install PAM config file:

mkdir -p "$RPM_BUILD_ROOT"/etc/pam.d
cp %{SOURCE1} "$RPM_BUILD_ROOT"/etc/pam.d/xscreensaver

[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ] \
    && rm -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"


%files -f xscreensaver.lang
%defattr(-, root, root)
%doc README*
%attr(0644, root, root) %config(noreplace) /etc/pam.d/xscreensaver
%{_bindir}/xscreensaver*
%{_mandir}/*/*.*
%{_libexecdir}/xscreensaver/
%{_libdir}/X11/app-defaults/XScreenSaver
%{_datadir}/applications/gnome-screensaver-properties.desktop
%{_datadir}/pixmaps/xscreensaver.xpm
%{_datadir}/xscreensaver/

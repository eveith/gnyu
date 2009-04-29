Name: lesstif
Version: 0.95.0
Release: 1ev
Summary: An open-source version of the Motif GUI toolkit
URL: http://www.lesstif.org/
Group: System Environment/Libraries
License: GPL-2, LGPL-2
Vendor: GNyU-Linux
Source: http://dl.sourceforge.net/sourceforge/lesstif/%{name}-%{version}.tar.bz2
BuildRequires: make, gcc, libX11, libICE, libXt, libXp, freetype
Requires: xorg-fslayout

%description
LessTif is the Hungry Programmers' version of OSF/Motif®. It aims to be 
source compatible meaning that the same source code should compile with 
both and work exactly the same! 


%prep
	%setup -q


%build
	%configure
	%{__make} %{?_smp_mflags}


%install
	%{__make} install DESTDIR='%{buildroot}'
	%{__rm} -rf '%{buildroot}/%{_prefix}/LessTif'


%post
	%{__ldconfig}


%postun
	%{__ldconfig}


%files
	%defattr(-, root, root)
	%doc README COPYING* AUTHORS BUG-REPORTING ChangeLog CREDITS FAQ doc
	%doc %{_bindir}/motif-config
	%doc %{_bindir}/mwm
	%doc %{_bindir}/mxmkmf
	%doc %{_bindir}/uil
	%doc %{_bindir}/xmbind
	%dir %{_includedir}/Mrm
	%{_includedir}/Mrm/*.h
	%dir %{_includedir}/uil
	%{_includedir}/uil/*.*
	%dir %{_includedir}/Dt
	%{_includedir}/Dt/*.h
	%dir %{_includedir}/Xm
	%{_includedir}/Xm/*.h
	%dir %{_libdir}/LessTif
	%dir %{_libdir}/LessTif/config
	%{_libdir}/LessTif/config/*.*
	%{_libdir}/X11/app-defaults/Mwm
	%dir %{_libdir}/X11/mwm
	%{_libdir}/X11/mwm/*
	%{_libdir}/libDtPrint.*
	%{_libdir}/libMrm.*
	%{_libdir}/libUil.*
	%{_libdir}/libXm.*
	%doc %{_mandir}/man1/lesstif.1*
	%doc %{_mandir}/man1/ltversion.1*
	%doc %{_mandir}/man1/mwm.1*
	%doc %{_mandir}/man1/uil.1*
	%doc %{_mandir}/man1/xmbind.1*
	%doc %{_mandir}/man3/ApplicationShell.3*
	%doc %{_mandir}/man3/Composite.3*
	%doc %{_mandir}/man3/Constraint.3*
	%doc %{_mandir}/man3/Core.3*
	%doc %{_mandir}/man3/LessTifInternals.3*
	%doc %{_mandir}/man3/Object.3*
	%doc %{_mandir}/man3/OverrideShell.3*
	%doc %{_mandir}/man3/Rect.3*
	%doc %{_mandir}/man3/Shell.3*
	%doc %{_mandir}/man3/TopLevelShell.3*
	%doc %{_mandir}/man3/TransientShell.3*
	%doc %{_mandir}/man3/UnNamedObj.3*
	%doc %{_mandir}/man3/VendorShell.3*
	%doc %{_mandir}/man3/WmShell.3*
	%doc %{_mandir}/man3/Xm*.3**
	%doc %{_mandir}/man5/VirtualBindings.5**
	%doc %{_mandir}/man5/mwmrc.5**
	%{_datadir}/aclocal/ac_find_motif.m4*

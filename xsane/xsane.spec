Name: xsane
Version: 0.997
Release: 3ev
Summary: A X frontend to SANE
License: GPL
Group: Applications/Productivity
Source: http://www.xsane.org/download/xsane-%{version}.tar.gz
URL: http://www.xsane.org
BuildRequires: pkg-config, make, gcc, gettext
BuildRequires: gtk2 >= 2.0.0, gimp >= 2.0.0, libjpeg, libpng, libtiff, lcms
BuildRequires: zlib
BuildRequires: sane-backends >= 1.0.0

%description
Xsane is a grahical frontend for sane. Install this if you want a grahpical
frontend for sane for use in the X Windowing System.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'
%find_lang xsane


%files -f xsane.lang
%defattr(-, root, root)
%doc xsane.*
%{_bindir}/xsane
%dir %{_datadir}/sane/xsane
%{_datadir}/sane/xsane/*
%{_datadir}/applications/xsane.desktop
%{_datadir}/pixmaps/xsane.xpm
%doc %{_mandir}/man1/xsane.1*

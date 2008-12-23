Name: xsane
Version: 0.996
Release: 2ev
Summary: A X frontend to SANE
License: GPL
Group: Applications/Productivity
Source: http://www.xsane.org/download/xsane-%{version}.tar.gz
URL: http://www.xsane.org/
Requires: sane-backends, gimp, libjpeg, libtiff, libpng, lcms
BuildRequires: make, gcc, gtk2

%description
Xsane is a grahical frontend for sane. Install this if you want a grahpical
frontend for sane for use in the X Windowing System.


%prep
%setup -q
%configure


%build
%{__make} %{?_smp_mflags}
%find_lang xsane


%install
%{__make_install} DESTDIR='%{buildroot}'
%find_lang xsane


%files -f xsane.lang
%defattr(-, root, root)
%doc xsane.*
%{_bindir}/xsane
%{_datadir}/sane/xsane/
%{_datadir}/applications/xsane.desktop
%{_datadir}/pixmaps/xsane.xpm
%doc %{_mandir}/man1/xsane.1*

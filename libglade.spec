Name: libglade
Version: 2.6.0
Release: 1ev
Summary: XML-based runtime user interface loader for GNOME.
URL: http://developer.gnome.org/doc/API/libglade/libglade.html
Group: System Environment/Libraries
License: LGPL
Vendor: MSP Slackware
Packager: Eric MSP Veith <eveith@wwweb-library.net>
Source: http://ftp.gnome.org/pub/GNOME/sources/%{name}/2.6/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: make >= 3.79.1, gcc-core, gtk2 >= 2.4.0, libxml2 >= 2.4.10
Provides: libtool(%{_libdir}/libglade-2.0.la)

%description
Libglade is a small library that allows a program to load its user interface
from an XML description at runtime. The XML file format is that of the user
interface builder GLADE, so libglade acts as an alternative to GLADE's code
generation approach. Libglade also provides a simple interface for connecting
handlers to the various signals in the interface (on platforms where the
gmodule library works correctly, it is possible to connect all the handlers
with a single function call). Once the interface has been instantiated,
libglade gives no overhead, so other than the initial interface loading time
(which is short), there is no performance tradeoff.


%prep
%setup -q


%build
%configure
make


%install
make install DESTDIR="$RPM_BUILD_ROOT"
rm -vf ${RPM_BUILD_ROOT}/%{_infodir}/dir


%post
/sbin/ldconfig
xmlcatalog --noout --add "system" \
	"http://glade.gnome.org/glade-2.0.dtd" \
	%{_datadir}/xml/libglade/*.dtd /etc/xml/catalog || true

%postun
xmlcatalog --noout --del "system" \
	"http://glade.gnome.org/glade-2.0.dtd" \
	%{_datadir}/xml/libglade/*.dtd /etc/xml/catalog || true
/sbin/ldconfig


%clean
rm -rf ${RPM_BUILD_ROOT}


%files
%defattr(-, root, root)
%doc README COPYING AUTHORS ChangeLog NEWS examples/
%doc %{_datadir}/gtk-doc/html/libglade/
%{_bindir}/libglade-convert
%{_includedir}/libglade-2.0/
%{_libdir}/libglade-2.0.*
%{_libdir}/pkgconfig/libglade-2.0.pc
%{_datadir}/xml/libglade/

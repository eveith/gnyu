Name: shared-mime-info
Version: 0.51
Release: 1ev
Summary: Core database of common MIME types (i. e. file formats)
URL: http://www.freedesktop.org/wiki/Software/shared-mime-info
Group: System Environment/Base
License: GPL-2
Vendor: GNyU-Linux
Source: http://freedesktop.org/~hadess/shared-mime-info-%{version}.tar.bz2
BuildRequires: make, gcc, glib2, intltool >= 0.35.0, gettext, perl, pkg-config
BuildRequires: libxml2, perl-XML-Parser

%description
Many programs and desktops use the MIME system to represent the types of files.
Frequently, it is necessary to work out the correct MIME type for a file. 
This is generally done by examining the file's name or contents, and looking 
up the correct MIME type in a database.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'
%find_lang shared-mime-info

%{__mkdir_p} '%{buildroot}/%{_libdir}'
%{__mv} '%{buildroot}/%{_datadir}/pkgconfig' '%{buildroot}/%{_libdir}'


%files -f shared-mime-info.lang
%defattr(-, root, root)
%doc ChangeLog COPYING HACKING NEWS README
%{_bindir}/update-mime-database
%{_libdir}/pkgconfig/shared-mime-info.pc
%doc %{_mandir}/man1/update-mime-database.1*
%dir %{_datadir}/mime
%{_datadir}/mime/*

Name: texinfo
Version: 4.13a
Release: 2.0ev
Summary: Tools needed to create Texinfo format documentation files.
Url: http://www.gnu.org/software/texinfo/
Group: Applications/Publishing
License: GPL-3
Vendor: GNyU-Linux
Source0: ftp://ftp.gnu.org/gnu/texinfo/texinfo-%{version}.tar.gz
Source2: texi2pdf.man
BuildRequires: make, gcc, gettext >= 0.17, zlib, ncurses
Requires: tetex
Provides: texinfo-tex = %{version}-%{release}

%description
Texinfo is a documentation system that can produce both online
information and printed output from a single source file. The GNU
Project uses the Texinfo file format for most of its documentation.
Install texinfo if you want a documentation system for producing both
online and print documentation from the same source file and/or if you
are going to write documentation for the GNU Project.


%package -n info
Summary: A stand-alone TTY-based reader for GNU texinfo documentation.
Group: System Environment/Base

%description -n info
The GNU project uses the texinfo file format for much of its
documentation. The info package provides a standalone TTY-based
browser program for viewing texinfo files.


%prep
%setup -q -n '%{name}-4.13'


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'
%find_lang '%{name}'
%{__touch} '%{buildroot}/%{_infodir}/dir'

pushd '%{buildroot}'
%{__install} -m644 '%{SOURCE2}' .%{_mandir}/man1/texi2pdf.1
%{__mkdir_p} ./sbin
%{__mv} .%{_bindir}/install-info ./sbin
popd


%post
update-info-dir


%preun
update-info-dir


%post -n info
update-info-dir


%preun -n info
update-info-dir


%files -f '%{name}.lang'
%defattr(-, root, root)
%doc AUTHORS ChangeLog INSTALL INTRODUCTION NEWS README TODO
%{_bindir}/makeinfo
%{_bindir}/pdftexi2dvi
%{_bindir}/texindex
%{_bindir}/texi2dvi
%{_bindir}/texi2pdf
%dir %{_datadir}/texinfo
%{_datadir}/texinfo/texinfo.cat
%{_datadir}/texinfo/texinfo.dtd
%{_datadir}/texinfo/texinfo.xsl
%doc %{_infodir}/texinfo*
%doc %{_mandir}/man1/makeinfo.1*
%doc %{_mandir}/man1/pdftexi2dvi.1*
%doc %{_mandir}/man1/texindex.1*
%doc %{_mandir}/man1/texi2dvi.1*
%doc %{_mandir}/man1/texi2pdf.1*
%doc %{_mandir}/man5/texinfo.5*


%files -n info
%defattr(-, root, root)
%ghost %config(noreplace) %verify(not md5 size mtime) %{_infodir}/dir
/sbin/install-info
%{_bindir}/info
%{_bindir}/infokey
%doc %{_infodir}/info.info*
%doc %{_infodir}/info-stnd.info*
%doc %{_mandir}/man1/info.1*
%doc %{_mandir}/man1/infokey.1*
%doc %{_mandir}/man1/install-info.1*
%doc %{_mandir}/man5/info.5*

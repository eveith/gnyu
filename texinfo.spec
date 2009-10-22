Summary: Tools needed to create Texinfo format documentation files.
Name: texinfo
Version: 4.8
Release: 1ev
License: GPL
Group: Applications/Publishing
Url: http://www.gnu.org/software/texinfo/
Source0: ftp://ftp.gnu.org/gnu/texinfo/texinfo-%{version}.tar.bz2
Source1: info-dir
Source2: texi2pdf.man
Patch1: texinfo-4.8-zlib.patch
Patch2: texinfo-CAN-2005-3011.patch
Prereq: /sbin/install-info
Prefix: %{_prefix}
Buildroot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: zlib, ncurses
Requires: tetex
Provides: texinfo-tex = %{version}-%{release}


# Redefine this so "dir" in the info directory isn't compressed

%define __spec_install_post %{?__debug_package:%{__debug_install_post}} /usr/lib/rpm/brp-strip \; /usr/lib/rpm/brp-strip-comment-note \; rm -f

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
# By making info prereq bash, other packages which have triggers based on
# info don't run those triggers until bash is in place as well. This is an
# ugly method of doing it (triggers which fire on set intersection would
# be better), but it's the best we can do for now. Talk to Erik before
# removing this.
Prereq: bash

%description -n info
The GNU project uses the texinfo file format for much of its
documentation. The info package provides a standalone TTY-based
browser program for viewing texinfo files.


%prep
%setup -q
%patch1 -p1 -b .zlib
%patch2 -p1 -b .CAN-2005-3011


%build
%configure
make %{?_smp_mflags}


%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}/sbin
make install DESTDIR=$RPM_BUILD_ROOT

pushd ${RPM_BUILD_ROOT}
  install -m644 %{SOURCE2} .%{_mandir}/man1/texi2pdf.1
  gzip -n -9f .%{_infodir}/*info*
  gzip -n -9f .%{_mandir}/*/*
  install -m644 $RPM_SOURCE_DIR/info-dir .%{_infodir}/dir
  mv -f .%{_bindir}/install-info ./sbin
popd

rm -f $RPM_BUILD_ROOT%{_datadir}/texinfo/texinfo.{xsl,dtd}

%find_lang %name


%clean
rm -rf ${RPM_BUILD_ROOT}


%post
/sbin/install-info %{_infodir}/texinfo.gz %{_infodir}/dir || :

%preun
if [ $1 = 0 ]; then
    /sbin/install-info --delete %{_infodir}/texinfo.gz %{_infodir}/dir || :
fi

%post -n info
/sbin/install-info %{_infodir}/info-stnd.info.gz %{_infodir}/dir || :

%preun -n info
if [ $1 = 0 ]; then
    /sbin/install-info --delete %{_infodir}/info-stnd.info.gz %{_infodir}/dir \
	|| :
fi


%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog INSTALL INTRODUCTION NEWS README TODO
%doc --parents info/README
%{_bindir}/makeinfo
%{_bindir}/texindex
%{_bindir}/texi2dvi
%{_bindir}/texi2pdf
%{_datadir}/texinfo
%{_infodir}/texinfo*
%{_mandir}/man1/makeinfo.1*
%{_mandir}/man1/texindex.1*
%{_mandir}/man1/texi2dvi.1*
%{_mandir}/man1/texi2pdf.1*
%{_mandir}/man5/texinfo.5*

%files -n info
%defattr(-,root,root)
%config(noreplace) %verify(not md5 size mtime) %{_infodir}/dir
%{_bindir}/info
%{_bindir}/infokey
%{_infodir}/info.info*
%{_infodir}/info-stnd.info*
/sbin/install-info
%{_mandir}/man1/info.1*
%{_mandir}/man1/infokey.1*
%{_mandir}/man1/install-info.1*
%{_mandir}/man5/info.5*

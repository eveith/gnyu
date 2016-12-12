Name: gettext
Version: 0.18.1.1
Release: 1.0
Summary: GNU libraries and utilities for multi-lingual messages
License: GPL/LGPL
Group: System Environment/Base
Source: ftp://ftp.gnu.org/gnu/gettext/%{name}-%{version}.tar.gz
URL: http://www.gnu.org/software/gettext
BuildRequires: grep, sed, gawk, make
BuildRequires: bison, gcc

%description
The GNU gettext package provides a set of tools and documentation for
producing multi-lingual messages in programs. Tools include a set of
conventions about how programs should be written to support message
catalogs, a directory and file naming organization for the message
catalogs, a runtime library which supports the retrieval of translated
messages, and stand-alone programs for handling the translatable and
the already translated strings. Gettext provides an easy to use
library and tools for creating, using, and modifying natural language
catalogs and is a powerful and simple method for internationalizing
programs.

%post 
%{__ldconfig}
if [ "$1" -eq 1 ]; then
    install-info %{_infodir}/autosprintf.info* '%{_infodir}/dir'
    install-info %{_infodir}/gettext.info* '%{_infodir}/dir'
fi

%preun
if [ "$1" -eq 1 ]; then
    install-info --delete %{_infodir}/autosprintf.info* '%{_infodir}/dir'
    install-info %{_infodir}/gettext.info* '%{_infodir}/dir'
fi

%postun -p %{__ldconfig}


%package tools
Summary: Tools and documentation for developers and translators
Group: Development/Tools
Requires: gettext

%description tools
As an addition to GNU gettext for developers, this package helps you to
develop internationalized applications and to translate existing messages.


%prep
%setup -q

# Fix perl path:
for file in gettext-runtime/libasprintf/texi2html \
		gettext-tools/doc/texi2html
do
	%{__sed} -i 's,#!/usr/local/bin/perl,#!%{__perl},g' "${file}"
done


%build
%configure \
    --with-included-libcroco \
	--without-emacs \
	--enable-shared 
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'
%{__rm} -f '%{buildroot}%{_infodir}/dir' ||:
%{__mv} '%{buildroot}%{_datadir}/doc' \
	"${RPM_BUILD_DIR}/%{name}-%{version}/Doc"

%find_lang gettext-runtime
%find_lang gettext-tools


%files -f gettext-runtime.lang
%defattr(-,root,root)
%doc gettext-runtime/ABOUT-NLS AUTHORS gettext-runtime/BUGS
%doc COPYING gettext-tools/misc/DISCLAIM README* NEWS THANKS
%doc gettext-runtime/man/*.html
%doc gettext-runtime/intl/COPYING*
%doc gettext-runtime/man/*.html
%doc gettext-runtime/intl-java/javadoc*/
%doc gettext-runtime/intl-csharp/csharpdoc/

%{_bindir}/gettext
%{_bindir}/ngettext
%{_bindir}/envsubst
%{_bindir}/gettext.sh

%doc %{_mandir}/man1/gettext.1*
%doc %{_mandir}/man1/ngettext.1*
%doc %{_mandir}/man1/envsubst.1*
%doc %{_mandir}/man3/gettext.3*
%doc %{_mandir}/man3/ngettext.3*
%doc %{_mandir}/man3/textdomain.3*
%doc %{_mandir}/man3/bindtextdomain.3*
%doc %{_mandir}/man3/bind_textdomain_codeset.3*
%doc %{_mandir}/man3/dgettext.3*
%doc %{_mandir}/man3/dcgettext.3*
%doc %{_mandir}/man3/dngettext.3*
%doc %{_mandir}/man3/dcngettext.3*

#%doc %{_infodir}/autosprintf.info*
%doc %{_infodir}/gettext.info*

#%{_libdir}/libasprintf*

%dir %{_datadir}/gettext
%{_datadir}/gettext/ABOUT-NLS


%files tools -f gettext-tools.lang
%doc gettext-tools/README* gettext-tools/ABOUT-NLS gettext-tools/AUTHORS
%doc gettext-tools/COPYING* gettext-tools/doc/ gettext-tools/examples/
%doc Doc/gettext/

%{_bindir}/msgcmp
%{_bindir}/msgfmt
%{_bindir}/msgmerge
%{_bindir}/msgunfmt
%{_bindir}/xgettext
%{_bindir}/msgattrib
%{_bindir}/msgcat
%{_bindir}/msgcomm
%{_bindir}/msgconv
%{_bindir}/msgen
%{_bindir}/msgexec
%{_bindir}/msgfilter
%{_bindir}/msggrep
%{_bindir}/msginit
%{_bindir}/msguniq
%{_bindir}/gettextize
%{_bindir}/autopoint
%{_bindir}/recode-sr-latin

%{_libdir}/libgettextlib-*.so
%{_libdir}/libgettextsrc-*.so
%{_libdir}/libgettextlib.*
%{_libdir}/libgettextsrc.*
%{_libdir}/libgettextpo*
%{_libdir}/preloadable_libintl.so

%{_datadir}/gettext/config.rpath
%{_datadir}/gettext/intl
%{_datadir}/gettext/po
%{_datadir}/gettext/projects
%{_datadir}/gettext/gettext.h
%{_datadir}/gettext/msgunfmt.tcl
%{_datadir}/gettext/javaversion.class
%{_datadir}/gettext/styles
%{_datadir}/gettext/archive.dir.tar.gz

%{_libdir}/gettext/

%doc %{_mandir}/man1/msgcmp.1*
%doc %{_mandir}/man1/msgfmt.1*
%doc %{_mandir}/man1/msgmerge.1*
%doc %{_mandir}/man1/msgunfmt.1*
%doc %{_mandir}/man1/xgettext.1*
%doc %{_mandir}/man1/msgattrib.1*
%doc %{_mandir}/man1/msgcat.1*
%doc %{_mandir}/man1/msgcomm.1*
%doc %{_mandir}/man1/msgconv.1*
%doc %{_mandir}/man1/msgen.1*
%doc %{_mandir}/man1/msgexec.1*
%doc %{_mandir}/man1/msgfilter.1*
%doc %{_mandir}/man1/msggrep.1*
%doc %{_mandir}/man1/msginit.1*
%doc %{_mandir}/man1/msguniq.1*
%doc %{_mandir}/man1/gettextize.1*
%doc %{_mandir}/man1/autopoint.1*
%doc %{_mandir}/man1/recode-sr-latin.1*

%{_datadir}/aclocal/*.m4

%{_includedir}/gettext-po.h
#%{_includedir}/autosprintf.h

#%{_libdir}/libasprintf.*a
#%{_libdir}/libasprintf.so

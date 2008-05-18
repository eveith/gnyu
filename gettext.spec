Name: gettext
Version: 0.17
Release: 1ev
Summary: GNU libraries and utilities for multi-lingual messages.
License: GPL/LGPL
Group: System Environment/Base
Source: ftp://ftp.gnu.org/gnu/gettext/%{name}-%{version}.tar.gz
URL: http://www.gnu.org/software/gettext/
Vendor: MSP Slackware
Source1: po-mode-init.el
Source2: msghack.py
Patch1: gettext-0.14.3-gcc4.patch
BuildRequires: libtool, bison, gcc-g++, gcc
Buildroot: %{_tmppath}/%{name}-%{version}-root

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


%package tools
Summary: Tools and documentation for developers and translators
Group: Development/Tools
Requires: gettext

%description tools
As an addition to GNU gettext for developers, this package helps you to
develop internationalized applications and to translate existing messages.


%prep
%setup -q
%patch1 -p1 -b .gcc4

%build
[[ -f  /usr/share/automake/depcomp ]] \
	&& %{__cp} -f /usr/share/automake/{depcomp,ylwrap} . || :

%configure \
	--enable-nls \
	--enable-shared 
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'
%{__install} -m 0755 %{SOURCE2} %{buildroot}/%{_bindir}/msghack
%{__rm} -f ${RPM_BUILD_ROOT}/%{_infodir}/dir
%{__mv} %{buildroot}/%{_datadir}/doc ${RPM_BUILD_DIR}/%{name}-%{version}/Doc

%find_lang gettext-runtime
%find_lang gettext-tools

%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%post
/sbin/ldconfig
exit 0

%postun
/sbin/ldconfig

%post tools
update-info-dir

%postun tools
update-info-dir


%files -f gettext-runtime.lang
%defattr(-,root,root)
%doc gettext-runtime/ABOUT-NLS AUTHORS gettext-runtime/BUGS
%doc COPYING gettext-tools/misc/DISCLAIM README* NEWS THANKS
%doc gettext-runtime/man/*.html
%doc gettext-runtime/intl/COPYING*
%doc gettext-runtime/man/*.html
%doc gettext-runtime/intl-java/javadoc*/
%doc gettext-runtime/intl-csharp/csharpdoc/
%{_mandir}/man1/gettext.1*
%{_mandir}/man1/ngettext.1*
%{_mandir}/man1/envsubst.1*
%{_mandir}/man3/gettext.3*
%{_mandir}/man3/ngettext.3*
%{_mandir}/man3/textdomain.3*
%{_mandir}/man3/bindtextdomain.3*
%{_mandir}/man3/bind_textdomain_codeset.3*
%{_mandir}/man3/dgettext.3*
%{_mandir}/man3/dcgettext.3*
%{_mandir}/man3/dngettext.3*
%{_mandir}/man3/dcngettext.3*
%{_libdir}/libasprintf*
%{_includedir}/autosprintf.h
%{_infodir}/autosprintf.info.gz
%{_bindir}/gettext
%{_bindir}/ngettext
%{_bindir}/envsubst
%{_bindir}/gettext.sh
%{_bindir}/msghack

%files tools -f gettext-tools.lang
%doc gettext-tools/README* gettext-tools/ABOUT-NLS gettext-tools/AUTHORS
%doc gettext-tools/COPYING* gettext-tools/doc/ gettext-tools/examples/
%doc Doc/gettext/
%{_datadir}/gettext/
%{_mandir}/man1/msgcmp.1*
%{_mandir}/man1/msgfmt.1*
%{_mandir}/man1/msgmerge.1*
%{_mandir}/man1/msgunfmt.1*
%{_mandir}/man1/xgettext.1*
%{_mandir}/man1/msgattrib.1*
%{_mandir}/man1/msgcat.1*
%{_mandir}/man1/msgcomm.1*
%{_mandir}/man1/msgconv.1*
%{_mandir}/man1/msgen.1*
%{_mandir}/man1/msgexec.1*
%{_mandir}/man1/msgfilter.1*
%{_mandir}/man1/msggrep.1*
%{_mandir}/man1/msginit.1*
%{_mandir}/man1/msguniq.1*
%{_mandir}/man1/gettextize.1*
%{_mandir}/man1/autopoint.1*
%{_mandir}/man1/recode-sr-latin.1*
%{_datadir}/aclocal/*.m4
%{_infodir}/gettext.info*
%{_libdir}/libgettextlib*
%{_libdir}/libgettextsrc*
%{_libdir}/preloadable_libintl.so
%{_libdir}/gettext/
%{_libdir}/libgettextpo*
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
%{_includedir}/gettext-po.h

Name: bogofilter
Version: 1.2.1
Release: 2.0ev
Summary: A Bayesian spam filter
URL: http://bogofilter.sourceforge.net/
Group: Applications/Internet
License: GPL-2, GPL-3
Vendor: GNyU-Linux
Source: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
BuildRequires: make, gcc, flex >= 2.5.3, db, xmlto, perl

%description
Bogofilter is a Bayesian spam filter. In its normal mode of operation, it
takes an email message or other text on standard input, does a statistical
check against lists of "good" and "bad" words, and returns a status code
indicating whether or not the message is spam. Bogofilter is designed with
fast algorithms (including Berkeley DB system), coded directly in C, and tuned
for speed, so it can be used for production by sites that process a lot of
mail.


%prep
%setup -q


%build
%configure \
	--with-database=db \
	--with-included-gsl
%{__make} %{?_smp_mflags} 


%install
%{__make} install DESTDIR="${RPM_BUILD_ROOT}"
%{__mv} "${RPM_BUILD_ROOT}/%{_sysconfdir}/bogofilter.cf.example" \
	"${RPM_BUILD_ROOT}/%{_sysconfdir}/bogofilter.cf"
[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ] \
    && rm -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"


%files
%defattr(-, root, root)
%doc AUTHORS COPYING GETTING.STARTED NEWS* README* RELEASE.NOTES TODO doc/
%config(noreplace) %{_sysconfdir}/bogofilter.cf
%{_bindir}/bf_compact
%{_bindir}/bf_copy
%{_bindir}/bf_tar
%{_bindir}/bogofilter
%{_bindir}/bogolexer
%{_bindir}/bogotune
%{_bindir}/bogoupgrade
%{_bindir}/bogoutil
%doc %{_mandir}/man1/bf_compact.1*
%doc %{_mandir}/man1/bf_copy.1*
%doc %{_mandir}/man1/bf_tar.1*
%doc %{_mandir}/man1/bogofilter.1*
%doc %{_mandir}/man1/bogolexer.1*
%doc %{_mandir}/man1/bogotune.1*
%doc %{_mandir}/man1/bogoupgrade.1*
%doc %{_mandir}/man1/bogoutil.1*

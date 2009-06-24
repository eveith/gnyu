Name: perl
Version: 5.10.0
Release: 2ev
Summary: The Practical Extraction and Report Language - a scripting language
URL: http://www.perl.org/
Group: Development/Languages
License: Artistic
Vendor: GNyU-Linux
Source: http://www.cpan.org/src/5.0/perl-%{version}.tar.gz
BuildRequires: gcc, make >= 3.79.1, sed, mktemp, gdbm, db
Provides: perl >= 1:5.8.0
Provides: perl >= 0:5.008001
Provides: perl(:MODULE_COMPAT_5.8.5)
Provides: perl(:MODULE_COMPAT_5.8.6)
Provides: perl(:MODULE_COMPAT_5.8.7)
Provides: perl(:MODULE_COMPAT_5.8.8)
Provides: perl(:WITH_ITHREADS)
Provides: perl(:WITH_THREADS)
Provides: perl(:WITH_LARGEFILES)
Provides: perl(:WITH_PERLIO)
Provides: perl(Carp::Heavy)
Provides: perl(FCGI)
Provides: perl(Mac::BuildTools)
Provides: perl(Mac::InternetConfig)
Provides: perl(NDBM_File)
Provides: perl(Tk)
Provides: perl(Tk::Pod)
Provides: perl(VMS::Filespec)
Provides: perl(VMS::Stdio)
Provides: perl(Your::Module::Here)
Provides: perl(bigint.pl)
Provides: perl(getopts.pl)
Provides: perl(timelocal.pl)
%define __perl_requires %nil


%description
Perl is a language that combines some of the features of C, sed, awk
and shell. Perl is a stable, cross platform programming language. 
It is used for mission critical projects in the public and private sectors. 
Perl is Open Source software, licensed under its Artistic License, or the GNU
General Public License (GPL). It was created by Larry Wall and is listed in 
the Oxford English Dictionary. ;^)


%prep
%setup -q


%build
%{__rm} -f config.sh Policy.sh
sh ./Configure \
	-de \
	-Dprefix='%{_prefix}' \
	-Dinstallprefix='%{_prefix}' \
	-Dvendorprefix='%{_prefix}' \
	-Dcccdlflags='-fPIC' \
	-Dcc="${CC:-%{_target_platform}-gcc}" \
	-Doptimize="$RPM_OPT_FLAGS" \
	-Darchname='%{_target_platform}' \
	-Duseshrplib \
	-Dusethreads \
	-Duseithreads \
	-Duselargefiles \
	-Duseperlio \
	-Di_gdbm \
	-Di_db \
	-Di_shadow \
	-Di_syslog \
	-Dman1dir='%{_mandir}/man1' \
	-Dman3dir='%{_mandir}/man3' \
	-Dman3ext=3pm \
	-Dcf_by='MSP Slackware'
%{__make} %{?_smp_mflags}
	

%install
%{__make} install DESTDIR='%{buildroot}'

# Create vendor and site extension dirs
arch=$(%{__grep} '^myarchname' ${RPM_BUILD_DIR}/%{name}-%{version}/config.sh |\
	%{__sed} "s,^myarchname='\(.*\)',\1,")
%{__mkdir_p} \
	"%{buildroot}/%{_libdir}/perl5/{vendor_perl,site_perl}/%{version}/$arch"

# Create the file list for the perl library dir
#find ${RPM_BUILD_ROOT}/usr/lib/perl5 -type d | \
#	sed "s,^${RPM_BUILD_ROOT}/usr/lib,\%dir \%{_libdir}," \
#	>> /tmp/rpmbuild-perl
#find ${RPM_BUILD_ROOT}/usr/lib/perl5 -not -type d | \
#	sed "s,^${RPM_BUILD_ROOT}/usr/lib,\%{_libdir}," \
#	>> /tmp/rpmbuild-perl


%files 
%defattr(-, root, root)
%doc README* Changes* AUTHORS Artistic Copying Todo* 
%{_bindir}/perl%{version}
%{_bindir}/perl
%{_bindir}/a2p
%{_bindir}/pod2html
%{_bindir}/pod2latex
%{_bindir}/pod2man
%{_bindir}/pod2text
%{_bindir}/pod2usage
%{_bindir}/podchecker
%{_bindir}/podselect
%{_bindir}/c2ph
%{_bindir}/cpan
%{_bindir}/config_data
%{_bindir}/corelist
%{_bindir}/dprofpp
%{_bindir}/enc2xs
%{_bindir}/h2ph
%{_bindir}/h2xs
%{_bindir}/instmodsh
%{_bindir}/libnetcfg
%{_bindir}/perlbug
%{_bindir}/perldoc
%{_bindir}/perlivp
%{_bindir}/piconv
%{_bindir}/pl2pm
%{_bindir}/prove
%{_bindir}/ptar
%{_bindir}/ptardiff
%{_bindir}/cpanp-run-perl
%{_bindir}/cpanp
%{_bindir}/cpan2dist
%{_bindir}/shasum
%{_bindir}/splain
%{_bindir}/xsubpp
%{_bindir}/find2perl
%{_bindir}/s2p
%{_bindir}/pstruct
%{_bindir}/psed
%{_libdir}/perl5/
%doc %{_mandir}/man1/*.1*
%doc %{_mandir}/man3/*.3*

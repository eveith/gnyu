Name: perl5.14
Version: 5.14.1
Release: 1.0
Summary: The Practical Extraction and Report Language - a scripting language
URL: http://www.perl.org/
Group: Development/Perl
License: Artistic
Vendor: GNyU-Linux
Source: http://www.cpan.org/src/5.0/perl-%{version}.tar.gz
BuildRequires: grep, sed, gawk, make
BuildRequires: gcc
BuildRequires: eglibc-devel, kernel-headers
BuildRequires: db-devel, tk-devel, gdbm
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
This is the main package containing the interpreter and documentation. It
creates a %{_bindir}/perl%{version} binary. If you want a %{_bindir}/perl link,
please install the corresponding "perl" package (without "5.14" in the name).


%files
%defattr(-, root, root)
%doc README* Changes* AUTHORS Artistic Copying
%{_bindir}/perl%{version}
%{_bindir}/a2p%{version}
%{_bindir}/pod2html%{version}
%{_bindir}/pod2latex%{version}
%{_bindir}/pod2man%{version}
%{_bindir}/pod2text%{version}
%{_bindir}/pod2usage%{version}
%{_bindir}/podchecker%{version}
%{_bindir}/podselect%{version}
%{_bindir}/cpan%{version}
%{_bindir}/config_data%{version}
%{_bindir}/corelist%{version}
%{_bindir}/dprofpp%{version}
%{_bindir}/enc2xs%{version}
%{_bindir}/instmodsh%{version}
%{_bindir}/json_pp%{version}
%{_bindir}/libnetcfg%{version}
%{_bindir}/perlbug%{version}
%{_bindir}/perldoc%{version}
%{_bindir}/perlivp%{version}
%{_bindir}/perlthanks%{version}
%{_bindir}/piconv%{version}
%{_bindir}/pl2pm%{version}
%{_bindir}/prove%{version}
%{_bindir}/ptar%{version}
%{_bindir}/ptardiff%{version}
%{_bindir}/cpanp-run-perl%{version}
%{_bindir}/cpanp%{version}
%{_bindir}/cpan2dist%{version}
%{_bindir}/shasum%{version}
%{_bindir}/splain%{version}
%{_bindir}/find2perl%{version}
%{_bindir}/s2p%{version}
%{_bindir}/pstruct%{version}
%{_bindir}/psed%{version}
%{_bindir}/ptargrep%{version}


%package -n perl
Summary: The Practical Extraction and Report Language - a scripting language
Group: Development/Perl
Requires: perl5.14 = %{version}-%{release}


%description -n perl
Perl is a language that combines some of the features of C, sed, awk
and shell. Perl is a stable, cross platform programming language. 
It is used for mission critical projects in the public and private sectors. 
Perl is Open Source software, licensed under its Artistic License, or the GNU
General Public License (GPL). It was created by Larry Wall and is listed in 
the Oxford English Dictionary. ;^)
This is a meta package containing only the %{_bindir}/perl binary. The main
package is perl5.14, which will be pulled in as a dependency.


%files -n perl
%defattr(-, root, root)
%doc README* Changes* AUTHORS Artistic Copying
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
%{_bindir}/json_pp
%{_bindir}/libnetcfg
%{_bindir}/perlbug
%{_bindir}/perldoc
%{_bindir}/perlivp
%{_bindir}/perlthanks
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
%{_bindir}/find2perl
%{_bindir}/s2p
%{_bindir}/pstruct
%{_bindir}/psed
%{_bindir}/ptargrep
%{_bindir}/xsubpp

%doc %{_mandir}/man1/a2p.1*
%doc %{_mandir}/man1/config_data.1*
%doc %{_mandir}/man1/corelist.1*
%doc %{_mandir}/man1/cpan.1*
%doc %{_mandir}/man1/cpan2dist.1*
%doc %{_mandir}/man1/cpanp.1*
%doc %{_mandir}/man1/find2perl.1*
%doc %{_mandir}/man1/instmodsh.1*
%doc %{_mandir}/man1/libnetcfg.1*
%doc %{_mandir}/man1/perl.1*
%doc %{_mandir}/man1/perlartistic.1*
%doc %{_mandir}/man1/perlbug.1*
%doc %{_mandir}/man1/pl2pm.1*
%doc %{_mandir}/man1/pod2html.1*
%doc %{_mandir}/man1/pod2latex.1*
%doc %{_mandir}/man1/pod2man.1*
%doc %{_mandir}/man1/pod2text.1*
%doc %{_mandir}/man1/pod2usage.1*
%doc %{_mandir}/man1/podchecker.1*
%doc %{_mandir}/man1/podselect.1*
%doc %{_mandir}/man1/prove.1*
%doc %{_mandir}/man1/psed.1*
%doc %{_mandir}/man1/ptar.1*
%doc %{_mandir}/man1/ptardiff.1*
%doc %{_mandir}/man1/ptargrep.1*
%doc %{_mandir}/man1/s2p.1*
%doc %{_mandir}/man1/shasum.1*
%doc %{_mandir}/man1/splain.1*



%package doc
Summary: Perl development documentation
Group: Development/Perl
Requires: %{name} = %{version}-%{release}


%description doc
Perl is a language that combines some of the features of C, sed, awk
and shell. Perl is a stable, cross platform programming language. 
If you intend to develop using Perl, this package provides you with the
modules and language documentation you'll probably need.


%files doc
%defattr(-, root, root)
%doc %{_mandir}/man3/*.3pm*

%doc %{_mandir}/man1/perlcall.1*
%doc %{_mandir}/man1/perlce.1*
%doc %{_mandir}/man1/perlcheat.1*
%doc %{_mandir}/man1/perlclib.1*
%doc %{_mandir}/man1/perlcn.1*
%doc %{_mandir}/man1/perlcommunity.1*
%doc %{_mandir}/man1/perlcompile.1*
%doc %{_mandir}/man1/perlcygwin.1*
%doc %{_mandir}/man1/perldata.1*
%doc %{_mandir}/man1/perldbmfilter.1*
%doc %{_mandir}/man1/dprofpp.1*
%doc %{_mandir}/man1/enc2xs.1*
%doc %{_mandir}/man1/json_pp.1*
%doc %{_mandir}/man1/perl*delta.1*
%doc %{_mandir}/man1/perlaix.1*
%doc %{_mandir}/man1/perlamiga.1*
%doc %{_mandir}/man1/perlapio.1*
%doc %{_mandir}/man1/perlbeos.1*
%doc %{_mandir}/man1/perlbook.1*
%doc %{_mandir}/man1/perlboot.1*
%doc %{_mandir}/man1/perlbot.1*
%doc %{_mandir}/man1/perlbs2000.1*
%doc %{_mandir}/man1/perlsymbian.1*
%doc %{_mandir}/man1/perlsyn.1*
%doc %{_mandir}/man1/perlthanks.1*
%doc %{_mandir}/man1/perlthrtut.1*
%doc %{_mandir}/man1/perltie.1*
%doc %{_mandir}/man1/perltoc.1*
%doc %{_mandir}/man1/perltodo.1*
%doc %{_mandir}/man1/perltooc.1*
%doc %{_mandir}/man1/perltoot.1*
%doc %{_mandir}/man1/perltrap.1*
%doc %{_mandir}/man1/perltru64.1*
%doc %{_mandir}/man1/perltw.1*
%doc %{_mandir}/man1/perlunicode.1*
%doc %{_mandir}/man1/perlunifaq.1*
%doc %{_mandir}/man1/perluniintro.1*
%doc %{_mandir}/man1/perluniprops.1*
%doc %{_mandir}/man1/perlunitut.1*
%doc %{_mandir}/man1/perlutil.1*
%doc %{_mandir}/man1/perluts.1*
%doc %{_mandir}/man1/perlvar.1*
%doc %{_mandir}/man1/perlvmesa.1*
%doc %{_mandir}/man1/perlvms.1*
%doc %{_mandir}/man1/perlvos.1*
%doc %{_mandir}/man1/perlwin32.1*
%doc %{_mandir}/man1/piconv.1*
%doc %{_mandir}/man1/perlpodspec.1*
%doc %{_mandir}/man1/perlpodstyle.1*
%doc %{_mandir}/man1/perlpolicy.1*
%doc %{_mandir}/man1/perlport.1*
%doc %{_mandir}/man1/perlpragma.1*
%doc %{_mandir}/man1/perlqnx.1*
%doc %{_mandir}/man1/perlre.1*
%doc %{_mandir}/man1/perlreapi.1*
%doc %{_mandir}/man1/perlrebackslash.1*
%doc %{_mandir}/man1/perlrecharclass.1*
%doc %{_mandir}/man1/perlref.1*
%doc %{_mandir}/man1/perlreftut.1*
%doc %{_mandir}/man1/perlreguts.1*
%doc %{_mandir}/man1/perlrequick.1*
%doc %{_mandir}/man1/perlreref.1*
%doc %{_mandir}/man1/perlretut.1*
%doc %{_mandir}/man1/perlriscos.1*
%doc %{_mandir}/man1/perlrun.1*
%doc %{_mandir}/man1/perlsec.1*
%doc %{_mandir}/man1/perlsolaris.1*
%doc %{_mandir}/man1/perlsource.1*
%doc %{_mandir}/man1/perlstyle.1*
%doc %{_mandir}/man1/perlsub.1*
%doc %{_mandir}/man1/perlintro.1*
%doc %{_mandir}/man1/perliol.1*
%doc %{_mandir}/man1/perlipc.1*
%doc %{_mandir}/man1/perlirix.1*
%doc %{_mandir}/man1/perlivp.1*
%doc %{_mandir}/man1/perljp.1*
%doc %{_mandir}/man1/perlko.1*
%doc %{_mandir}/man1/perllexwarn.1*
%doc %{_mandir}/man1/perllinux.1*
%doc %{_mandir}/man1/perllocale.1*
%doc %{_mandir}/man1/perllol.1*
%doc %{_mandir}/man1/perlmacos.1*
%doc %{_mandir}/man1/perlmacosx.1*
%doc %{_mandir}/man1/perlmod.1*
%doc %{_mandir}/man1/perlmodinstall.1*
%doc %{_mandir}/man1/perlmodlib.1*
%doc %{_mandir}/man1/perlmodstyle.1*
%doc %{_mandir}/man1/perlmpeix.1*
%doc %{_mandir}/man1/perlmroapi.1*
%doc %{_mandir}/man1/perlnetware.1*
%doc %{_mandir}/man1/perlnewmod.1*
%doc %{_mandir}/man1/perlnumber.1*
%doc %{_mandir}/man1/perlobj.1*
%doc %{_mandir}/man1/perlop.1*
%doc %{_mandir}/man1/perlopenbsd.1*
%doc %{_mandir}/man1/perlopentut.1*
%doc %{_mandir}/man1/perlos2.1*
%doc %{_mandir}/man1/perlos390.1*
%doc %{_mandir}/man1/perlos400.1*
%doc %{_mandir}/man1/perlpacktut.1*
%doc %{_mandir}/man1/perlperf.1*
%doc %{_mandir}/man1/perlplan9.1*
%doc %{_mandir}/man1/perlpod.1*
%doc %{_mandir}/man1/perldebtut.1*
%doc %{_mandir}/man1/perldebug.1*
%doc %{_mandir}/man1/perldgux.1*
%doc %{_mandir}/man1/perldiag.1*
%doc %{_mandir}/man1/perldoc.1*
%doc %{_mandir}/man1/perldos.1*
%doc %{_mandir}/man1/perldsc.1*
%doc %{_mandir}/man1/perlepoc.1*
%doc %{_mandir}/man1/perlfaq.1*
%doc %{_mandir}/man1/perlfaq1.1*
%doc %{_mandir}/man1/perlfaq2.1*
%doc %{_mandir}/man1/perlfaq3.1*
%doc %{_mandir}/man1/perlfaq4.1*
%doc %{_mandir}/man1/perlfaq5.1*
%doc %{_mandir}/man1/perlfaq6.1*
%doc %{_mandir}/man1/perlfaq7.1*
%doc %{_mandir}/man1/perlfaq8.1*
%doc %{_mandir}/man1/perlfaq9.1*
%doc %{_mandir}/man1/perlfilter.1*
%doc %{_mandir}/man1/perlfork.1*
%doc %{_mandir}/man1/perlform.1*
%doc %{_mandir}/man1/perlfreebsd.1*
%doc %{_mandir}/man1/perlfunc.1*
%doc %{_mandir}/man1/perlgit.1*
%doc %{_mandir}/man1/perlglossary.1*
%doc %{_mandir}/man1/perlgpl.1*
%doc %{_mandir}/man1/perlhaiku.1*
%doc %{_mandir}/man1/perlhist.1*
%doc %{_mandir}/man1/perlhpux.1*
%doc %{_mandir}/man1/perlhurd.1*


%package libs
Summary: Perl core libraries
Group: Development/Perl


%description libs
Perl is a language that combines some of the features of C, sed, awk
and shell. Perl is a stable, cross platform programming language. 
This package contains the Perl core modules that come with the original Perl
distribution.


%files libs
%defattr(-, root, root)

%dir %{_libdir}/perl5
%dir %{_libdir}/perl5/%{version}
%{_libdir}/perl5/%{version}/*

%dir %{_libdir}/perl5/site_perl
%dir %{_libdir}/perl5/site_perl/%{version}
%dir %{_libdir}/perl5/site_perl/%{version}/%{_target_cpu}-%{_host_vendor}-linux-*

%dir %{_libdir}/perl5/vendor_perl
%dir %{_libdir}/perl5/vendor_perl/%{version}




%package devel
Summary: Perl-to-C development files
Group: Development/Perl
Requires: %{name} = %{version}-%{release}


%description
Perl is a language that combines some of the features of C, sed, awk
and shell. Perl is a stable, cross platform programming language. 
The -devel package is useful when you intend to either extend Perl with C/C++
code, create an interface from C/C++ libraries already existing to Perl or want 
to embed the Perl interpreter in a C/C++ program of yours. You do not need
this package if you want to create Perl scripts.


%files devel
%defattr(-, root, root)
%doc README* Changes* AUTHORS Artistic Copying

%{_bindir}/c2ph%{version}
%{_bindir}/h2ph%{version}
%{_bindir}/h2xs%{version}
%{_bindir}/xsubpp%{version}

%doc %{_mandir}/man1/c2ph.1*
%doc %{_mandir}/man1/h2ph.1*
%doc %{_mandir}/man1/h2xs.1*
%doc %{_mandir}/man1/xsubpp.1*
%doc %{_mandir}/man1/perlapi.1*
%doc %{_mandir}/man1/perlguts.1*
%doc %{_mandir}/man1/perlhack.1*
%doc %{_mandir}/man1/perlhacktips.1*
%doc %{_mandir}/man1/perlhacktut.1*
%doc %{_mandir}/man1/perlxs.1*
%doc %{_mandir}/man1/perlxstut.1*
%doc %{_mandir}/man1/pstruct.1*
%doc %{_mandir}/man1/perlintern.1*
%doc %{_mandir}/man1/perlinterp.1*
%doc %{_mandir}/man1/perldebguts.1*
%doc %{_mandir}/man1/perlebcdic.1*
%doc %{_mandir}/man1/perlembed.1*



%prep
%setup -q -n 'perl-%{version}'


%build
%{__rm} config.sh Policy.sh ||:
%{__sh} ./Configure \
	-de \
	-Dprefix='%{_prefix}' \
	-Dinstallprefix='%{_prefix}' \
	-Dvendorprefix='%{_prefix}' \
	-Dcccdlflags='-fPIC' \
	-Dcc="${CC:-%{_target_platform}-gcc}" \
	-Doptimize='%{optflags}' \
	-Darchname='%{_target_platform}' \
	-Duseshrplib='true' \
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
    -Dcf_by='GNyU-Linux'
%{__make} %{?_smp_mflags}
	

%install
%{__make} install DESTDIR='%{buildroot}'

# Create vendor and site extension dirs
arch=$(%{__grep} '^myarchname' \
        "${RPM_BUILD_DIR}/%{name}-%{version}/config.sh" | \
    	%{__sed} "s,^myarchname='\(.*\)',\1,")
%{__mkdir_p} \
	'%{buildroot}%{_libdir}/perl5'/{vendor_perl,site_perl}/"%{version}/${arch}"

# Rename and create links for binaries.

pushd '%{buildroot}%{_bindir}'
%{__find} . -type f -not -name \*%{version} -not -name perl5\* \
    -exec %{__mv} '{}' '{}%{version}' \;
for i in *%{version}; do
    target=${i%*%{version}}
    [ -f "${target}" ] && continue
    %{__ln_s} "${i}" "${target}"
done
popd

# Create the file list for the perl library dir
#find ${RPM_BUILD_ROOT}/usr/lib/perl5 -type d | \
#	sed "s,^${RPM_BUILD_ROOT}/usr/lib,\%dir \%{_libdir}," \
#	>> /tmp/rpmbuild-perl
#find ${RPM_BUILD_ROOT}/usr/lib/perl5 -not -type d | \
#	sed "s,^${RPM_BUILD_ROOT}/usr/lib,\%{_libdir}," \
#	>> /tmp/rpmbuild-perl


%check
%{__make} test ||:

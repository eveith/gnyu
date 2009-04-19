Name: git
Version: 1.6.2.3
Release: 1ev
Summary: A distributed source code management system
URL: http://git-scm.org/
Group: Development/Tools
License: GPL-2
Vendor: GNyU-Linux
Source: http://kernel.org/pub/software/scm/git/git-%{version}.tar.bz2
BuildRequires: make, gcc, perl, openssl, curl, expat, openssh, zlib
Requires: openssh, perl

%description


%prep
	%setup -q


%build
	%configure \
		--without-tcltk
	%{__make} %{?_smp_mflags}


%install
	%{__make} install DESTDIR='%{buildroot}'

	# Move manpages *sigh*
	%{__mv} '%{buildroot}/%{_datadir}/man' '%{buildroot}/%{_mandir}' ||:

	# Remove Perl files we do not ship
	%{__rm} -rf '%{buildroot}/%{perl_archlib}'
	%{__rm} -rf '%{buildroot}/%{perl_sitearch}'


%files
	%defattr(-, root, root)
	%doc README COPYING Documentation/*.txt Documentation/howto
	%doc Documentation/technical
	%{_bindir}/git
	%{_bindir}/git-cvsserver
	%{_bindir}/git-receive-pack
	%{_bindir}/git-shell
	%{_bindir}/git-upload-archive
	%{_bindir}/git-upload-pack
	%{perl_sitelib}/Error.pm
	%{perl_sitelib}/Git.pm
	%dir %{_libexecdir}/git-core
	%{_libexecdir}/git-core/git-*
	%dir %{_datadir}/git-core
	%dir %{_datadir}/git-core/templates
	%{_datadir}/git-core/templates/description
	%dir %{_datadir}/git-core/templates/hooks
	%{_datadir}/git-core/templates/hooks/*.sample
	%dir %{_datadir}/git-core/templates/info
	%{_datadir}/git-core/templates/info/exclude
	%doc %{_mandir}/man3/Git.3pm
	%doc %{_mandir}/man3/private-Error.3pm

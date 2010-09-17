Name: cvs
Version: 1.12.13
Release: 2.0ev
Summary: A versioning system similar to RCS, but network-aware
URL: http://www.nongnu.org/cvs/
Group: Development/Tools
License: GPL-2
Vendor: GNyU-Linux
Source: http://ftp.gnu.org/non-gnu/cvs/source/feature/%{version}/cvs-%{version}.tar.bz2
BuildRequires: make, gcc, perl
BuildRequires: openssl, heimdal-libs, zlib
BuildRequires: vim, openssh
%define cvsadmin_gid 31

%description
CVS is a version control system, an important component of Source
Configuration Management (SCM). Using it, you can record the history of
sources files, and documents


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
	&& %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post
if [[ "${1}" -eq 1 ]]
then
	%{__groupadd} \
		-g '%{cvsadmin_gid}' \
		cvsadmin
fi
update-info-dir


%postun
if [[ "${1}" -eq 0 ]]
then
	%{__groupdel} cvsadmin
fi
update-info-dir


%files
%defattr(-, root, root)
%doc AUTHORS BUGS COPYING* DEVEL-CVS FAQ HACKING NEWS PROJECTS README*
%doc TESTS TODO
%{_bindir}/cvs
%{_bindir}/cvsbug
%{_bindir}/rcs2log
%doc %{_infodir}/cvs.info*
%doc %{_infodir}/cvsclient.info*
%doc %{_mandir}/man1/cvs.1*
%doc %{_mandir}/man5/cvs.5*
%doc %{_mandir}/man8/cvsbug.8*
%dir %{_datadir}/cvs
%dir %{_datadir}/cvs/contrib
%doc %{_datadir}/cvs/contrib/README
%{_datadir}/cvs/contrib/check_cvs
%{_datadir}/cvs/contrib/clmerge
%{_datadir}/cvs/contrib/cln_hist
%{_datadir}/cvs/contrib/commit_prep
%{_datadir}/cvs/contrib/cvs2vendor
%{_datadir}/cvs/contrib/cvs_acls
%{_datadir}/cvs/contrib/cvscheck
%{_datadir}/cvs/contrib/debug_check_log
%{_datadir}/cvs/contrib/intro.doc
%{_datadir}/cvs/contrib/log
%{_datadir}/cvs/contrib/log_accum
%{_datadir}/cvs/contrib/mfpipe
%{_datadir}/cvs/contrib/pvcs2rcs
%{_datadir}/cvs/contrib/rcs-to-cvs
%{_datadir}/cvs/contrib/rcs2log
%{_datadir}/cvs/contrib/rcslock
%{_datadir}/cvs/contrib/sccs2rcs

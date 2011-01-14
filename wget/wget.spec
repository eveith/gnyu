Name: wget 
Version: 1.11.4
Release: 2ev
Summary: A network utility for downloading content from the Web.
URL: http://www.gnu.org/software/wget
Group: Applications/Internet
License: GPL-3
Vendor: GNyU-Linux
Source: http://ftp.gnu.org/pub/gnu/wget/wget-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: make >= 3.79.1, gcc, openssl, gettext

%description
GNU Wget is a utility for noninteractive download of files from the Web. It
supports HTTP and FTP protocols, as well as retrieval through HTTP proxies. It
can follow HTML links, download many pages, and convert the links for local
viewing. It can also mirror FTP hierarchies or only those files that have
changed. Wget has been designed for robustness over slow network connections;
if a download fails due to a network problem, it will keep retrying until the
whole file has been retrieved.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR="${RPM_BUILD_ROOT}"
%{__rm} -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"
%find_lang wget


%post
update-info-dir

%postun
update-info-dir


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files -f wget.lang
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog* README* MAILING-LIST NEWS
%config(noreplace) %{_sysconfdir}/wgetrc
%{_bindir}/wget
%doc %{_infodir}/wget.info*
%doc %{_mandir}/man1/wget.1*

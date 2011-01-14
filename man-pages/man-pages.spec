Name: man-pages
Version: 3.22
Release: 2ev
Summary: The Linux manpages collection
URL: http://www.win.tue.nl/~aeb/linux/man/
Group: Documentation
License: Freely distributable
Vendor: GNyU-Linux
Source: ftp://ftp.win.tue.nl/pub/linux-local/manpages/%{name}-%{version}.tar.gz
BuildRequires: coreutils, findutils, bzip2
BuildArch: noarch

%description
The manpages package contains a large collection of man pages for Linux
covering programming APIs, file formats, protocols, etc. 


%prep
%setup -q


%build
exit 0


%install
%{__mkdir_p} '%{buildroot}/%{_mandir}'
%{__cp} -r -v man? '%{buildroot}/%{_mandir}'

# We need to remove some man pages which are already provided by other
# packages.
for r in man2/fgetxattr.2 man2/flistxattr.2 man2/fremovexattr.2 \
		man2/fsetxattr.2 man2/getxattr.2 man2/lgetxattr.2 man2/listxattr.2 \
		man2/llistxattr.2 man2/lremovexattr.2 man2/lsetxattr.2 man2/msgop.2 \
		man2/removexattr.2 man2/setxattr.2 man3/err.3 man3/getifaddrs.3 \
		man3/getspnam.3 man3/rand.3 man5/passwd.5
do
	%{__rm} -v "${r}"
done

# Bzip2 to save space.
%{__find} '%{buildroot}/%{_mandir}' -type f -name \*.\? \
		-exec %{__bzip2} -9 -v '{}' \;


%files
%defattr(-, root, root)
%doc Changes* README
%doc %attr(0644, root, man) %{_mandir}/man*/*.*

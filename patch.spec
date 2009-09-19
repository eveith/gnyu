Name: patch
Version: 2.5.9
Release: 2ev
Summary: An utility to apply difference listings to text files
URL: http://www.gnu.org/software/patch
Group: System Environment/Base
License: GPL-2
Vendor: GNyU-Linux
Source: ftp://ftp.gnu.org/pub/gnu/patch/patch-%{version}.tar.gz
BuildRequires: make, gcc

%description
`patch' takes a patch file containing a difference listing produced by 
diff and applies those differences to one or more original files, producing 
patched versions.
This version of `patch' has many changes made by the Free Software Foundation.
They add support for:
 * handling arbitrary binary data and large files
 * the unified context diff format that GNU diff can produce
 * making GNU Emacs-style backup files
 * improved interaction with RCS and SCCS
 * the GNU conventions for option parsing and configuring and compilation.
 * better POSIX.2 compliance


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags} ed_PROGRAM=vim


%install
%{__mkdir_p} '%{buildroot}'/{bin,'%{_mandir}/man1'}
%{__install} -m0755 patch '%{buildroot}/bin'
%{__install} -m0644 patch.man '%{buildroot}/%{_mandir}/man1/patch.1'


%files
%defattr(-, root, root)
%doc README NEWS AUTHORS ChangeLog
%{__patch}
%doc %{_mandir}/man1/patch.1*

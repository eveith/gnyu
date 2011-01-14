Name: xorg-fslayout
Version: 7.3
Release: 1ev
Summary: Xorg X11 file system layout
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Buildroot: %{_tmppath}/%{name}-buildroot
BuildArch: noarch
Provides: x11-fslayout = %{version}-%{release}

%description
The Xorg server and programs require a particular set of directories to be
present. This meta-package provides those directories, and even some other for
X-based programs that are often needed. Installing this package will thereof
create all directories most commonly needed for X11 applications.

%prep
exit 0


%build
exit 0

%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__mkdir_p} '%{buildroot}/%{_includedir}/GL'
%{__mkdir_p} '%{buildroot}/%{_includedir}/GL/internal'
%{__mkdir_p} '%{buildroot}/%{_includedir}/X11'
%{__mkdir_p} '%{buildroot}/%{_includedir}/X11/extensions'
%{__mkdir_p} '%{buildroot}/%{_includedir}/X11/PM'
%{__mkdir_p} '%{buildroot}/%{_includedir}/X11/dri'
%{__mkdir_p} '%{buildroot}/%{_includedir}/X11/fonts'


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%dir %{_includedir}/GL
%dir %{_includedir}/GL/internal
%dir %{_includedir}/X11
%dir %{_includedir}/X11/extensions
%dir %{_includedir}/X11/PM
%dir %{_includedir}/X11/dri
%dir %{_includedir}/X11/fonts

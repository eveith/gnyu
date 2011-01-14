Name: ccache
Version: 2.4
Release: 3ev
Summary: A caching C preprocessor
URL: http://ccache.samba.org/
Group: Development/Tools
License: GPL-2
Source: http://samba.org/ftp/ccache/ccache-%{version}.tar.gz
BuildRequires: make, gcc

%description
Ccache is a compiler cache. It acts as a caching pre-processor to C/C++
compilers, using the -E compiler switch and a hash to detect when a
compilation can be satisfied from cache. This often results in a 5 to 10 times
speedup in common compilations.
The idea came from Erik Thiele wrote the original compilercache program as a
bourne shell script. ccache is a re-implementation of Erik's idea in C with
more features and better performance.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'


%files
%defattr(-, root, root)
%doc COPYING README
%{_bindir}/ccache
%doc %{_mandir}/man1/ccache.1*

Name: ccache
Version: 2.4
Release: 2ev
Summary: A caching C preprocessor
License: GPL
Source: http://samba.org/ftp/ccache/ccache-2.4.tar.gz
URL: http://ccache.samba.org/
Group: Development/Tools
BuildRoot: %{_tmppath}/%{name}-root

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
make


%install
%makeinstall


%files
%defattr(-, root, root)
%doc COPYING README
%{_bindir}/ccache
%{_mandir}/man1/ccache.1.gz

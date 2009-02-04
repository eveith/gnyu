Name: clucene-core
Version: 0.9.21b
Release: 1ev
Summary: A text search engine written in C++
URL: http://clucene.sourceforge.net/
Group: System Environment/Libraries
License: LGPL-2.1 or Apache-2.0
Vendor: GNyU-Linux
Source: http://downloads.sourceforge.net/clucene/clucene-core-%{version}.tar.bz2
BuildRequires: make, gcc-g++

%description
CLucene is a high-performance, scalable, cross platform, full-featured, open-source 
indexing and searching API. It is written in C++.
CLucene is a port of the very popular Java Lucene text search engine API. 
Specifically, CLucene is the guts of a search engine, the hard stuff. You write the 
easy stuff, the UI and the process of selecting and parsing your data files to pump 
them into the search engine yourself.
CLucene aims to be a good alternative to Java Lucene when performance really matters 
or if you want to stick to good old C++.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{?__fakeroot} %{__make} install DESTDIR='%{buildroot}'

%post
%{__ldconfig}

%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc APACHE.license AUTHORS ChangeLog COPYING HACKING LGPL.license NEWS README
%doc REQUESTS
%{_includedir}/CLucene.h
%dir %{_includedir}/CLucene
%{_includedir}/CLucene/*
%{_libdir}/CLucene/clucene-config.h
%{_libdir}/libclucene.*

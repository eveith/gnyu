Name: strigi
Version: 0.6.4
Release: 1ev
Summary: A desktop search program
URL: http://strigi.sourceforge.net/
Group: System Environment/Daemons
License: LGPL-2
Vendor: GNyU-Linux
Source: http://downloads.sourceforge.net/strigi/strigi-%{version}.tar.bz2
BuildRequires: cmake >= 2.4.2, make, gcc-g++, clucene-core >= 0.9.16, file
BuildRequires: libxml2, bzip2, zlib, perl, dbus, qt4, pkg-config, java-jdk

%description
Strigi is a daemon which uses a very fast and efficient crawler that can 
index data on your harddrive. Indexing operations are performed without 
hammering your system, this makes Strigi the fastest and smallest desktop 
searching program.
Strigi can index different file formats, including the contents of the 
archive files. Strigi can be run from different OS and window manager. 
It has been written focusing on portability and extendability.


%prep
%setup -q


%build
%{cmake} \
	-DENABLE_CLUCENE:BOOL=ON \
	-DENABLE_CPPUNIT:BOOL=OFF \
	-DENABLE_DBUS:BOOL=ON \
	-DENABLE_HYPERESTRAIER:BOOL=OFF \
	-DENABLE_FAM:BOOL=OFF \
	-DENABLE_EXPAT:BOOL=ON \
	-DENABLE_LOG4CXX:BOOL=OFF \
	-DENABLE_EXIV2:BOOL=ON \
	-DENABLE_INOTIFY:BOOL=ON \
	-DENABLE_SQLITE:BOOL=OFF \
	.
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'


%post
%{__ldconfig}

%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING NEWS README TODO TODOMONDAY TODO.Phreedom
%{_bindir}/deepfind
%{_bindir}/deepgrep
%{_bindir}/luceneindexer
%{_bindir}/strigiclient
%{_bindir}/strigicmd
%{_bindir}/strigidaemon
%{_bindir}/xmlindexer
%dir %{_includedir}/strigi
%{_includedir}/strigi/*
%{_libdir}/libsearchclient.*
%{_libdir}/libstreams.*
%{_libdir}/libstreamanalyzer.*
%{_libdir}/libstrigihtmlgui.*
%{_libdir}/libstrigiqtdbusclient.*
%{_libdir}/pkgconfig/libstreamanalyzer.pc
%{_libdir}/pkgconfig/libstreams.pc
%dir %{_libdir}/strigi
%{_libdir}/strigi/*
%{_datadir}/dbus-1/services/org.freedesktop.xesam.searcher.service
%{_datadir}/dbus-1/services/vandenoever.strigi.service
%dir %{_datadir}/strigi
%{_datadir}/strigi/*

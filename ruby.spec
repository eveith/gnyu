Name: ruby
Version: 1.9.1
Release: 3ev
Summary: An interpreted script programing language (Ruby)
URL: http://www.ruby-lang.org/
Group: Development/Languages
License: GPL-2
Vendor: GNyU-Linux
Source: ftp://ftp.ruby-lang.org/pub/ruby/1.8/%{name}-%{version}-p0.tar.bz2
BuildRequires: make, gcc, groff, openssl
BuildRequires: libtermcap, ncurses, zlib, db, libX11, readline, zlib

%description
Ruby is the interpreted scripting language for quick and
easy object-oriented programming.  It has many features to
process text files and to do system management tasks (as in
Perl).  It is simple, straight-forward, and extensible.

Features of Ruby:
  + Simple Syntax
  + *Normal* Object-Oriented features(ex. class, method calls)
  + *Advanced* Object-Oriented features(ex. Mix-in, Singleton-method)
  + Operator Overloading
  + Exception Handling
  + Iterators and Closures
  + Garbage Collection
  + Dynamic Loading of Object files(on some architecture)
  + Highly Portable(works on many UNIX machines, and on DOS,
    Windows, Mac, BeOS etc.)


%prep
%setup -q -n '%{name}-%{version}-p0'


%build
%configure \
	--enable-pthread \
	--enable-shared \
	--enable-install-doc
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'


%post
%{__ldconfig}

%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc README* COPYING* GPL LEGAL LGPL NEWS ToDo
%{_bindir}/ruby
%{_bindir}/testrb
%{_bindir}/rdoc
%{_bindir}/erb
%{_bindir}/gem
%{_bindir}/rake
%{_bindir}/ri
%{_bindir}/irb
%{_libdir}/*ruby*.*
%dir %{_libdir}/ruby
%{_libdir}/ruby/%{version}/
%dir %{_includedir}/ruby-%{version}
%{_includedir}/ruby-%{version}/*
%doc %{_mandir}/man1/ruby.1*
%dir %{_datadir}/ri
%dir %{_datadir}/ri/%{version}/
%{_datadir}/ri/%{version}/*
%doc %{_mandir}/man1/erb.1*
%doc %{_mandir}/man1/irb.1*
%doc %{_mandir}/man1/rake.1*
%doc %{_mandir}/man1/ri.1*

Name: ruby
Version: 1.9.2
%define patchlevel 136
Release: 9.1ev
Summary: An interpreted script programing language (Ruby)
URL: http://www.ruby-lang.org/
Group: Development/Languages
License: GPL-2
Vendor: GNyU-Linux
Source: ftp://ftp.ruby-lang.org/pub/ruby/1.9/%{name}-%{version}-p%{patchlevel}.tar.gz
BuildRequires: make, gcc, gcc-g++, binutils,
BuildRequires: doxygen, groff
BuildRequires: openssl, readline, ncurses, zlib, db, libX11
Requires: ruby-libs = %{version}-%{release}

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


%package libs
Summary: Ruby's core libraries and the corresponding directory structure
Group: System Environment/Libraries
Requires: libruby1.9 = %{version}-%{release}

%description libs
This is the Ruby language's core library, as well as the directory structure
needed for Ruby gems (i.e., addon-libraries for ruby). For the API
documentation, see the %{name}-doc package.


%package -n libruby1.9
Summary: Ruby C library
Group: System Environment/Libraries
Conflicts: ruby-libs < 1.9.2

%description -n libruby1.9
This library represents Ruby's C part and is used to embed the interpreter.


%package doc
Summary: API documentation for Ruby developers
Group: Development/Documentation
Requires: ruby = %{version}-%{release}

%description doc
This package contains the complete API documentation of Ruby, in both RI and
HTML format, along with the "ri" command line utility.


%package devel
Summary: Ruby development headers
Group: Development/Libraries
Requires: libruby1.9 = %{version}-%{release}

%description devel
Header files and libraries for building a extension library for the Ruby or an
application embedded Ruby.


%prep
%setup -q -n '%{name}-%{version}-p%{patchlevel}'


%build
%configure \
	--with-ruby-version=full \
	--enable-shared \
	--enable-install-doc \
	--with-mantype=man
%{__make} %{?_smp_mflags}


%check
%{__make} test


%install
%{__make} install DESTDIR='%{buildroot}'
%{__mkdir_p} \
	'%{buildroot}/%{_libdir}/ruby/site_ruby/%{version}/%{_target}'
%{__mkdir_p} \
	'%{buildroot}/%{_libdir}/ruby/vendor_ruby/%{version}/%{_target}'


%post -n libruby1.9
%{__ldconfig}


%postun -n libruby1.9
%{__ldconfig}


%files
%defattr(-, root, root)
%doc README* COPYING* GPL LEGAL NEWS ToDo
%{_bindir}/ruby
%{_bindir}/testrb
%{_bindir}/rdoc
%{_bindir}/erb
%{_bindir}/gem
%{_bindir}/rake
%{_bindir}/irb
%doc %{_mandir}/man1/ruby.1*
%doc %{_mandir}/man1/erb.1*
%doc %{_mandir}/man1/irb.1*
%doc %{_mandir}/man1/rake.1*


%files libs
%defattr(-, root, root)
%doc README* COPYING* GPL LEGAL NEWS ToDo
%dir %{_libdir}/ruby
%dir %{_libdir}/ruby/1.9.?
%dir %{_libdir}/ruby/gems
%dir %{_libdir}/ruby/gems/1.9.?
%dir %{_libdir}/ruby/gems/1.9.?/specifications
%{_libdir}/ruby/gems/1.9.?/*/*
%dir %{_libdir}/ruby/site_ruby
%dir %{_libdir}/ruby/site_ruby/1.9.?
%dir %{_libdir}/ruby/site_ruby/1.9.?/%{_target}
%dir %{_libdir}/ruby/vendor_ruby
%dir %{_libdir}/ruby/vendor_ruby/1.9.?
%dir %{_libdir}/ruby/vendor_ruby/1.9.?/%{_target}
%{_libdir}/ruby/1.9.?/*


%files doc
%defattr(-, root, root)
%doc README* COPYING* GPL LEGAL NEWS ToDo
%{_bindir}/ri
%doc %{_mandir}/man1/ri.1*
%dir %{_datadir}/ri
%dir %{_datadir}/ri/1.9.?/
%doc %{_datadir}/ri/1.9.?/*
%dir %{_datadir}/doc/ruby
%dir %{_datadir}/doc/ruby/html
%doc %{_datadir}/doc/ruby/html/*



%files -n libruby1.9
%defattr(-, root, root)
%doc README* COPYING* GPL LEGAL NEWS ToDo
%{_libdir}/libruby.so*


%files devel
%defattr(-, root, root)
%doc README* COPYING* GPL LEGAL NEWS ToDo
%dir %{_includedir}/ruby-1.9.?
%{_includedir}/ruby-1.9.?/*
%{_libdir}/libruby-static.a

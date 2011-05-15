Name: ruby1.9
Version: 1.9.2
%define patchlevel 180
Release: 1.0
Summary: An interpreted script programing language (Ruby)
URL: http://www.ruby-lang.org
Group: Development/Languages
License: GPL-2
Source: ftp://ftp.ruby-lang.org/pub/ruby/1.9/ruby-%{version}-p%{patchlevel}.tar.gz
BuildRequires: grep, sed, make, gcc, gcc-g++
BuildRequires: eglibc-devel
BuildRequires: doxygen, groff
BuildRequires: openssl-devel, readline-devel, ncurses-devel
BuildRequires: zlib-devel, db-devel, libX11
Requires: ruby1.9-libs = %{version}-%{release}

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

This package contains the interpreter and some auxillary programs, postfixed
with "1.9" to allow multiple versions of Ruby to be installed in parallel. If
you want to have a single "ruby" executable, install the "ruby" package at any
available version.


%package -n ruby
Summary: An interpreted script programing language (Ruby)
Group: Development/Languages
Requires: ruby1.9 = %{version}-%{release}

%description -n ruby
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
Requires: libruby1.9 = %{version}-%{release}, ruby1.9 = %{version}-%{release}

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
Requires: ruby1.9 = %{version}-%{release}

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
%setup -q -n 'ruby-%{version}-p%{patchlevel}'


%build
%configure \
	--enable-shared \
	--enable-install-doc \
	--with-mantype=man
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'
%{__mkdir_p} \
	'%{buildroot}%{_libdir}/ruby/site_ruby/%{version}/%{_target}'
%{__mkdir_p} \
	'%{buildroot}%{_libdir}/ruby/vendor_ruby/%{version}/%{_target}'

for i in ruby testrb rdoc erb gem rake irb; do
    %{__mv} "%{buildroot}%{_bindir}/${i}" \
        "%{buildroot}%{_bindir}/${i}-1.9"
    %{__ln_s} "%{_bindir}/${i}-1.9" \
        "%{buildroot}%{_bindir}/${i}"

    manfile="%{buildroot}%{_mandir}/man1/${i}.1"
    [ -f "${manfile}" ] || continue
    %{__mv} "$manfile" "%{buildroot}%{_mandir}/man1/${i}-1.9.1.1"
    %{__ln_s} "%{_mandir}/man1/${i}-1.9.1.1" \
        "${manfile}"
done


%check
%{__make} test


%post -n libruby1.9 -p %{__ldconfig}
%postun -n libruby1.9 -p %{__ldconfig}


%files
%defattr(-, root, root)
%doc README* COPYING* GPL LEGAL NEWS ToDo
%{_bindir}/ruby-1.9
%{_bindir}/testrb-1.9
%{_bindir}/rdoc-1.9
%{_bindir}/erb-1.9
%{_bindir}/gem-1.9
%{_bindir}/rake-1.9
%{_bindir}/irb-1.9
%doc %{_mandir}/man1/ruby-1.9.1*
%doc %{_mandir}/man1/erb-1.9.1*
%doc %{_mandir}/man1/irb-1.9.1*
%doc %{_mandir}/man1/rake-1.9.1*


%files -n ruby
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
%{_libdir}/libruby.so.1.9*


%files devel
%defattr(-, root, root)
%doc README* COPYING* GPL LEGAL NEWS ToDo
%dir %{_includedir}/ruby-1.9.?
%{_includedir}/ruby-1.9.?/*
%{_libdir}/libruby-static.a
%{_libdir}/libruby.so

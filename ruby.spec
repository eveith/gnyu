Name: ruby
Version: 1.9.1
%define patchlevel 243
Release: 7.0ev
Summary: An interpreted script programing language (Ruby)
URL: http://www.ruby-lang.org/
Group: Development/Languages
License: GPL-2
Vendor: GNyU-Linux
Source: ftp://ftp.ruby-lang.org/pub/ruby/1.9/%{name}-%{version}-p%{patchlevel}.tar.gz
BuildRequires: make, gcc, groff
BuildRequires: openssl, readline, ncurses, zlib, db, libX11

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


%package -n libruby1.9
Summary: Ruby language library
Group: System Environment/Libraries
Provides: libruby = %{version}
Obsoletes: libruby < %{version}

%description -n libruby1.9
This is the Ruby language's core library. It contains the standard language
features which are required to run Ruby script. libruby is often linked to by
programs that want to embed Ruby or parse the language.


%prep
	%setup -q -n '%{name}-%{version}-p%{patchlevel}'


%build
	%configure \
		--enable-pthread \
		--enable-shared \
		--enable-install-doc
	%{__make} %{?_smp_mflags}


%check
	%{__make} test


%install
	%{__make} install DESTDIR='%{buildroot}'
	%{__mkdir_p} \
		'%{buildroot}/%{_libdir}/ruby/site_ruby/%{version}/%{_target}'
	%{__mkdir_p} \
		'%{buildroot}/%{_libdir}/ruby/vendor_ruby/%{version}/%{_target}'


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
	%dir %{_libdir}/ruby
	%dir %{_libdir}/ruby/%{version}
	%dir %{_libdir}/ruby/site_ruby
	%dir %{_libdir}/ruby/site_ruby/%{version}
	%dir %{_libdir}/ruby/site_ruby/%{version}/%{_target}
	%dir %{_libdir}/ruby/vendor_ruby
	%dir %{_libdir}/ruby/vendor_ruby/%{version}
	%dir %{_libdir}/ruby/vendor_ruby/%{version}/%{_target}
	%{_libdir}/ruby/%{version}/*
	%dir %{_includedir}/ruby-%{version}
	%{_includedir}/ruby-%{version}/*
	%dir %{_datadir}/ri
	%dir %{_datadir}/ri/%{version}/
	%doc %{_datadir}/ri/%{version}/*
	%doc %{_mandir}/man1/ruby.1*
	%doc %{_mandir}/man1/erb.1*
	%doc %{_mandir}/man1/irb.1*
	%doc %{_mandir}/man1/rake.1*
	%doc %{_mandir}/man1/ri.1*


%files -n libruby1.9
	%{_libdir}/*ruby*.*

Name: ruby
Version: 1.8.7
%define patchlevel 173
Release: 5ev
Summary: An interpreted script programing language (Ruby)
URL: http://www.ruby-lang.org/
Group: Development/Languages
License: GPL-2
Vendor: GNyU-Linux
Source: ftp://ftp.ruby-lang.org/pub/ruby/1.8/%{name}-%{version}-p%{patchlevel}.tar.gz
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


%package -n libruby1.8
Summary: Ruby language library
Group: System Environment/Libraries

%description -n libruby1.8
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
	#%{_bindir}/gem
	#%{_bindir}/rake
	%{_bindir}/ri
	%{_bindir}/irb
	%dir %{_libdir}/ruby
	%{_libdir}/ruby/?.?/
	#%dir %{_includedir}/ruby-?.?
	#%{_includedir}/ruby-?.?/*
	%dir %{_datadir}/ri
	%dir %{_datadir}/ri/?.?/
	%{_datadir}/ri/?.?/*
	%doc %{_mandir}/man1/ruby.1*
	#%doc %{_mandir}/man1/erb.1*
	#%doc %{_mandir}/man1/irb.1*
	#%doc %{_mandir}/man1/rake.1*
	#%doc %{_mandir}/man1/ri.1*


%files -n libruby1.8
	%{_libdir}/*ruby*.*

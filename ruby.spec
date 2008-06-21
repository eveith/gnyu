Name: ruby
Version: 1.8.6
Release: 1ev
Summary: The Ruby Programing Language
URL: http://www.ruby-lang.org/
Group: Development/Languages
License: GPL-2
Vendor: MSP Slackware
Source: ftp://ftp.ruby-lang.org/pub/ruby/1.8/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, groff, openssl, libtermcap, ncurses, zlib, db
BuildRequires: libX11

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
%setup -q


%build
%configure \
	--enable-shared \
	--enable-install-doc
make %{_smp_mflags}


%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"

[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ] \
    && rm -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-, root, root)
%doc README* COPYING* GPL LEGAL LGPL NEWS ToDo
%{_bindir}/ruby
%{_bindir}/testrb
%{_bindir}/rdoc
%{_bindir}/erb
%{_bindir}/ri
%{_bindir}/irb
%{_libdir}/*ruby*.*
%dir %{_libdir}/ruby
%{_libdir}/ruby/1.8/
%{_mandir}/man1/ruby.1*
%dir %{_datadir}/ri
%{_datadir}/ri/1.8/

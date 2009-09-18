Name: fribidi
Version: 0.10.9
Release: 1ev
Summary: An implementation of the Unicode Bidirectional Algorithm (bidi)
URL: http://fribidi.org/
Group: System Environment/Libraries
License: LGPL-2.1
Vendor: GNyU-Linux
Source: http://fribidi.org/download/fribidi-%{version}.tar.gz
BuildRequires: make, gcc, pkg-config

%description
The Unicode Standard prescribes a memory representation order known as logical
order. When text is presented in horizontal lines, most scripts display
characters from left to right. However, there are several scripts (such as
Arabic or Hebrew) where the natural ordering of horizontal text in display is
from right to left. If all of the text has the same horizontal direction, then
the ordering of the display text is unambiguous. However, when bidirectional
text (a mixture of left-to-right and right-to-left horizontal text) is
present, some ambiguities can arise in determining the ordering of the
displayed characters.
The bidi algorithm tries to solve that. fribidi is an implementation of that
algorithm.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'


[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post
%{__ldconfig}


%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc AUTHORS COPYING README NEWS TODO
%{_bindir}/fribidi
%{_bindir}/fribidi-config
%dir %{_includedir}/fribidi
%{_includedir}/fribidi/*.h
%{_includedir}/fribidi/*.i
%{_libdir}/libfribidi.*
%{_libdir}/pkgconfig/fribidi.pc

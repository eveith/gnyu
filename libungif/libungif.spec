Name: libungif
Version: 4.1.4
Release: 1ev
Summary: A modified, patent-free version of giflib for reading GIF images
URL: http://directory.fsf.org/project/libungif/
Group: System Environment/Libraries
License: X11
Vendor: GNyU-Linux
Source http://downloads.sourceforge.net/giflib/libungif-%{version}.tar.gz
BuildRequires: make, gcc, libX11

%description
The libungif library is a specially modified version of giflib which is free
of the Unisys LZW patent. It can read all GIFs, but only write uncompressed
GIFs.


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
	%doc AUTHORS BUGS ChangeLog COPYING DEVELOPERS *NEWS README TODO
	%doc UNCOMPRESSED_GIF
	%{_bindir}/gif2epsn
	%{_bindir}/gif2ps
	%{_bindir}/gif2rgb
	%{_bindir}/gif2rle
	%{_bindir}/gif2x11
	%{_bindir}/gifasm
	%{_bindir}/gifbg
	%{_bindir}/gifburst
	%{_bindir}/gifclip
	%{_bindir}/gifclrmp
	%{_bindir}/gifcolor
	%{_bindir}/gifcomb
	%{_bindir}/gifcompose
	%{_bindir}/giffiltr
	%{_bindir}/giffix
	%{_bindir}/gifflip
	%{_bindir}/gifhisto
	%{_bindir}/gifinfo
	%{_bindir}/gifinter
	%{_bindir}/gifinto
	%{_bindir}/gifovly
	%{_bindir}/gifpos
	%{_bindir}/gifrotat
	%{_bindir}/gifrsize
	%{_bindir}/gifspnge
	%{_bindir}/giftext
	%{_bindir}/gifwedge
	%{_bindir}/icon2gif
	%{_bindir}/raw2gif
	%{_bindir}/rgb2gif
	%{_bindir}/rle2gif
	%{_bindir}/text2gif
	%{_includedir}/gif_lib.h
	%{_libdir}/libungif.*

Summary: A library to access and alter JPEG images
Name: libjpeg
Version: 6b
Release: 1ev
Group: System Environment/Libraries
Source: http://www.ijg.org/files/jpegsrc.v6b.tar.gz
URL: http://www.ijg.org/
License: LGPL-alike
Vendor: GNyU-Linux

%description
This package contains C software to implement JPEG image compression and
decompression.  JPEG (pronounced "jay-peg") is a standardized compression
method for full-color and gray-scale images.  JPEG is intended for compressing
"real-world" scenes; line drawings, cartoons and other non-realistic images
are not its strong suit.  JPEG is lossy, meaning that the output image is not
exactly identical to the input image.  Hence you must not use JPEG if you
have to have identical output bits.  However, on typical photographic images,
very good compression levels can be obtained with no visible change, and
remarkably high compression levels are possible if you can tolerate a
low-quality image.  For more details, see the references, or just experiment
with various compression settings.


%prep
%setup -qn jpeg-6b


%build
%configure \
	--enable-shared \
	--enable-static
%{__make} %{?_smp_mflags}


%install
%{__mkdir_p} \
	"$RPM_BUILD_ROOT"/{'%{_libdir}','%{_bindir}',%{_includedir},%{_mandir}/man1}
%{__make} install \
	prefix="$RPM_BUILD_ROOT/%{_prefix}" \
	exec_prefix="$RPM_BUILD_ROOT/%{_prefix}" \
	bindir="$RPM_BUILD_ROOT/%{_bindir}" \
	libdir="$RPM_BUILD_ROOT/%{_libdir}" \
	includedir="$RPM_BUILD_ROOT/%{_includedir}" \
	mandir="$RPM_BUILD_ROOT/%{_mandir}/man1"


%post
%{__ldconfig}

%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc README
%{_includedir}/jconfig.h
%{_includedir}/jpeglib.h
%{_includedir}/jmorecfg.h
%{_includedir}/jerror.h
%{_libdir}/libjpeg.so.62.0.0
%{_libdir}/libjpeg.so.62
%{_libdir}/libjpeg.so
%{_libdir}/libjpeg.la
%{_libdir}/libjpeg.a
%{_bindir}/cjpeg
%{_bindir}/djpeg
%{_bindir}/jpegtran
%{_bindir}/rdjpgcom
%{_bindir}/wrjpgcom
%doc %{_mandir}/man1/cjpeg.1*
%doc %{_mandir}/man1/djpeg.1*
%doc %{_mandir}/man1/jpegtran.1*
%doc %{_mandir}/man1/rdjpgcom.1*
%doc %{_mandir}/man1/wrjpgcom.1*

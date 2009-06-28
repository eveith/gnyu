Name: libzip
Version: 0.9
Release: 1ev
Summary: A C library for reading, creating, and modifying zip archives
URL: http://www.nih.at/libzip/
Group: System Environment/Libraries
License: Unknown
Vendor: GNyU-Linux
Source: http://www.nih.at/libzip/libzip-%{version}.tar.bz2
BuildRequires: make, gcc, zlib

%description
libzip is a C library for reading, creating, and modifying zip archives. Files
can be added from data buffers, files, or compressed data copied directly from
other zip archives. Changes made without closing the archive can be reverted.
The API is documented by man pages.


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
	%doc THANKS TODO AUTHORS NEWS README
	%{_bindir}/zipcmp
	%{_bindir}/zipmerge
	%{_bindir}/ziptorrent
	%{_includedir}/zip.h
	%{_libdir}/libzip.*
	%{_libdir}/pkgconfig/libzip.pc
	%doc %{_mandir}/man1/zipcmp.1*
	%doc %{_mandir}/man1/zipmerge.1*
	%doc %{_mandir}/man1/ziptorrent.1*
	%doc %{_mandir}/man3/libzip.3*
	%doc %{_mandir}/man3/zip_add.3*
	%doc %{_mandir}/man3/zip_add_dir.3*
	%doc %{_mandir}/man3/zip_close.3*
	%doc %{_mandir}/man3/zip_delete.3*
	%doc %{_mandir}/man3/zip_error_clear.3*
	%doc %{_mandir}/man3/zip_error_get.3*
	%doc %{_mandir}/man3/zip_error_get_sys_type.3*
	%doc %{_mandir}/man3/zip_error_to_str.3*
	%doc %{_mandir}/man3/zip_errors.3*
	%doc %{_mandir}/man3/zip_fclose.3*
	%doc %{_mandir}/man3/zip_file_error_clear.3*
	%doc %{_mandir}/man3/zip_file_error_get.3*
	%doc %{_mandir}/man3/zip_file_strerror.3*
	%doc %{_mandir}/man3/zip_fopen.3*
	%doc %{_mandir}/man3/zip_fopen_index.3*
	%doc %{_mandir}/man3/zip_fread.3*
	%doc %{_mandir}/man3/zip_get_archive_comment.3*
	%doc %{_mandir}/man3/zip_get_archive_flag.3*
	%doc %{_mandir}/man3/zip_get_file_comment.3*
	%doc %{_mandir}/man3/zip_get_name.3*
	%doc %{_mandir}/man3/zip_get_num_files.3*
	%doc %{_mandir}/man3/zip_name_locate.3*
	%doc %{_mandir}/man3/zip_open.3*
	%doc %{_mandir}/man3/zip_rename.3*
	%doc %{_mandir}/man3/zip_replace.3*
	%doc %{_mandir}/man3/zip_set_archive_comment.3*
	%doc %{_mandir}/man3/zip_set_archive_flag.3*
	%doc %{_mandir}/man3/zip_set_file_comment.3*
	%doc %{_mandir}/man3/zip_source_buffer.3*
	%doc %{_mandir}/man3/zip_source_file.3*
	%doc %{_mandir}/man3/zip_source_filep.3*
	%doc %{_mandir}/man3/zip_source_free.3*
	%doc %{_mandir}/man3/zip_source_function.3*
	%doc %{_mandir}/man3/zip_source_zip.3*
	%doc %{_mandir}/man3/zip_stat.3*
	%doc %{_mandir}/man3/zip_stat_index.3*
	%doc %{_mandir}/man3/zip_stat_init.3*
	%doc %{_mandir}/man3/zip_strerror.3*
	%doc %{_mandir}/man3/zip_unchange.3*
	%doc %{_mandir}/man3/zip_unchange_all.3*
	%doc %{_mandir}/man3/zip_unchange_archive.3*

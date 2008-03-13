Name: cyrus-sasl
Version: 2.1.22
Release: 1ev
Summary: A generic client/server library for SASL authentication
URL: http://asg.web.cmu.edu/sasl/
Group: System Environment/Libraries
License: BSD
Vendor: MSP Slackware
Source: ftp://ftp.andrew.cmu.edu/pub/cyrus-mail/cyrus-sasl-%{version}.tar.gz
BuildRequires: gcc-core, make >= 3.79.1, openssl, db >= 4.5, libgcj
BuildRequires: heimdal-libs, libpam
Requires: openssl, heimdal-libs, libpam
Buildroot: %{_tmppath}/%{name}-root
Provides: libtool(%{_libdir}/sasl2/libsasldb.la)
Provides: libtool(%{_libdir}/sasl2/libcrammd5.la)
Provides: libtool(%{_libdir}/sasl2/libdigestmd5.la)
Provides: libtool(%{_libdir}/sasl2/libotp.la)
Provides: libtool(%{_libdir}/sasl2/libgssapiv2.la)
Provides: libtool(%{_libdir}/sasl2/libplain.la)
Provides: libtool(%{_libdir}/sasl2/libanonymous.la)
Provides: libtool(%{_libdir}/libsasl2.la)
Provides: libtool(%{_libdir}/libjavasasl.la)

%description
The Cyrus SASL library is a generic library for easy integration of secure
network authentication to any client or server application. It supports
authentication via standard plaintext methods as well as CRAM-MD5 and
DIGEST-MD5 shared secret methods and KERBEROS_V4 and GSSAPI Kerberos methods.
The SASL protocol framework is used by SMTP, IMAP, ACAP, LDAP, and other
standard protocols.


%prep
%setup -q


%build
# Adjust include/library path for kerberos
export CPPFLAGS="$CPPFLAGS $(krb5-config --cflags)"
CFLAGS="$CFLAGS $(krb5-config --libs) $(krb5-config --cflags)"
CXXFLAGS="$CXXFLAGS $(krb5-config --libs) $(krb5-config --cflags)"

%configure \
	--with-dbpath=/%{_sysconfdir}/sasldb2 \
	--with-pwcheck=/%{_localstatedir}/run \
	--with-saslauthd=/%{_localstatedir}/run \
	--with-authdaemond=/%{_localstatedir}/run \
	--enable-java \
	--enable-checkapop \
	--enable-cram \
	--enable-digest \
	--enable-gssapi \
	--enable-gss_mutexes \
	--enable-plain \
	--enable-anon \
	--enable-login 
%{__make} %{_smp_mflags}


%install
[[ "$RPM_BUILD_ROOT" != "/" ]] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"

rm -vf ${RPM_BUILD_ROOT}/%{_infodir}/dir

# Create saslauthd startup file

mkdir -p ${RPM_BUILD_ROOT}/etc/initng/daemon
mkdir -p ${RPM_BUILD_ROOT}/etc/conf.d/cyrus-sasl

cat << EOF > ${RPM_BUILD_ROOT}/etc/initng/daemon/saslauthd.i
#!/sbin/itype

daemon daemon/saslauthd {
	need = virtual/net system/bootmisc
	script daemon = {
		# Read options

		opts='-d'

		# options with value first

		[ -r "/etc/conf.d/cyrus-sasl/authd_authmech" ] \\
			&& opts="\$opts -a \$(< /etc/conf.d/cyrus-sasl/authd_authmech)"
		[ -r "/etc/conf.d/cyrus-sasl/authd_numprocesses" ] \\
            && opts="\$opts -n \$(< /etc/conf.d/cyrus-sasl/authd_numprocesses)"
		[ -r "/etc/conf.d/cyrus-sasl/authd_workingdir" ] \\
            && opts="\$opts -m \$(< /etc/conf.d/cyrus-sasl/authd_workingdir)"

		# Now boolean options

		[ -e "/etc/conf.d/cyrus-sasl/authd_docredentialscaching" ] \\
			&& opts="\$opts -c"
		[ -e "/etc/conf.d/cyrus-sasl/authd_docacceptlocking" ] \\
            && opts="\$opts -l"

		# Whatever else there may be, add it here
		
		[ -e "/etc/conf.d/cyrus-sasl/authd_options" ] \\
			&& opts="\$opts \$(< /etc/conf.d/cyrus-sasl/authd_options)"

		exec %{_sbindir}/saslauthd "\$opts"
	};
}
EOF

# Touch available startup options, so the user nows what he may set.

mkdir -p ${RPM_BUILD_ROOT}/etc/conf.d/cyrus-sasl/Options
for file in authd_authmech authd_numprocesses authd_workingdir \
		authd_docredentialscaching authd_docacceptlocking authd_options
do
	touch ${RPM_BUILD_ROOT}/etc/conf.d/cyrus-sasl/Options/$file
done


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[[ "$RPM_BUILD_ROOT" != "/" ]] && rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-, root, root)
%doc README* AUTHORS COPYING ChangeLog NEWS
/etc/conf.d/cyrus-sasl/
/etc/initng/daemon/saslauthd.i
%{_includedir}/sasl/
%{_libdir}/java/classes/sasl/
%{_libdir}/libjavasasl.*
%{_libdir}/libsasl2.*
%{_libdir}/sasl2/
%{_mandir}/*/*
%{_sbindir}/pluginviewer
%{_sbindir}/saslauthd
%{_sbindir}/sasldblistusers2
%{_sbindir}/saslpasswd2
%{_sbindir}/testsaslauthd
%{_sbindir}/pwcheck

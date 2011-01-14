Name: libical
Version: 0.43
Release: 1ev
Summary: An open source reference implementation of the icalendar data type
URL: http://sourceforge.net/projects/freeassociation/
Group: System Environment/Libraries
License: LGPL-2.1, MPL
Vendor: GNyU-Linux
Source: http://downloads.sourceforge.net/freeassociation/libical-%{version}.tar.gz
BuildRequires: make, gcc, gcc-g++, flex, bison, libstdc++

%description
This is an implementation of iCalendar protocols and data formats.


%package cxx
Summary: C++ bindings for libical, an icalender reference implementation
Requires: libical

%description
This is an implementation of iCalendar protocols and data formats.
%{name}-cxx contains the C++ bindings to libical.


%prep
%setup -q


%build
%configure \
	--enable-cxx
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post
%{__ldconfig}

%postun
%{__ldconfig}

%post cxx
%{__ldconfig}

%postun cxx
%{__ldconfig}


%files
%defattr(-, root, root)
%doc COPYING ChangeLog LICENSE NEWS README TEST THANKS TODO
%{_includedir}/ical.h
%dir %{_includedir}/libical
%{_includedir}/libical/ical.h               
%{_includedir}/libical/icalarray.h          
%{_includedir}/libical/icalattach.h         
%{_includedir}/libical/icalcalendar.h       
%{_includedir}/libical/icalclassify.h       
%{_includedir}/libical/icalcluster.h        
%{_includedir}/libical/icalcomponent.h      
%{_includedir}/libical/icalderivedparameter.h
%{_includedir}/libical/icalderivedproperty.h 
%{_includedir}/libical/icalderivedvalue.h    
%{_includedir}/libical/icaldirset.h          
%{_includedir}/libical/icaldirsetimpl.h      
%{_includedir}/libical/icalduration.h        
%{_includedir}/libical/icalenums.h           
%{_includedir}/libical/icalerror.h           
%{_includedir}/libical/icalfileset.h         
%{_includedir}/libical/icalfilesetimpl.h     
%{_includedir}/libical/icalgauge.h           
%{_includedir}/libical/icalgaugeimpl.h       
%{_includedir}/libical/icallangbind.h        
%{_includedir}/libical/icalmemory.h          
%{_includedir}/libical/icalmessage.h         
%{_includedir}/libical/icalmime.h            
%{_includedir}/libical/icalparameter.h       
%{_includedir}/libical/icalparser.h          
%{_includedir}/libical/icalperiod.h
%{_includedir}/libical/icalproperty.h
%{_includedir}/libical/icalrecur.h
%{_includedir}/libical/icalrestriction.h
%{_includedir}/libical/icalset.h
%{_includedir}/libical/icalspanlist.h
%{_includedir}/libical/icalss.h
%{_includedir}/libical/icalssyacc.h
%{_includedir}/libical/icaltime.h
%{_includedir}/libical/icaltimezone.h
%{_includedir}/libical/icaltypes.h
%{_includedir}/libical/icaltz-util.h
%{_includedir}/libical/icalvalue.h
%{_includedir}/libical/icalvcal.h
%{_includedir}/libical/port.h
%{_includedir}/libical/pvl.h
%{_includedir}/libical/sspm.h
%{_includedir}/libical/vcaltmp.h
%{_includedir}/libical/vcc.h
%{_includedir}/libical/vobject.h
%{_libdir}/libical.*
%{_libdir}/libicalss.*
%{_libdir}/libicalvcal.*
%{_libdir}/pkgconfig/libical.pc

%files cxx
%defattr(-, root, root)
%doc COPYING ChangeLog LICENSE NEWS README TEST THANKS TODO
%{_includedir}/libical/icalparameter_cxx.h
%{_includedir}/libical/icalproperty_cxx.h
%{_includedir}/libical/icalvalue_cxx.h
%{_includedir}/libical/icptrholder.h
%{_includedir}/libical/vcomponent.h
%{_libdir}/libical_cxx.*
%{_libdir}/libicalss_cxx.*

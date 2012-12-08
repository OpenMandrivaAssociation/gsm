%define	srcver	1.0-pl13

%define	major	1
%define libname	%mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Shared libraries for GSM speech compressor
Name:		gsm
Version:	1.0.13
Release:	%mkrel 6
Group:		System/Libraries
License:	distributable
URL:		http://www.quut.com/gsm/
Source0:	http://www.quut.com/gsm/%{name}-%{version}.tar.gz
Patch0:         gsm-1.0.10-dyn.patch
Patch1:         gsm-1.0-pl10-includes.patch
Patch3:         gsm-1.0-pl10-shared.diff
Patch4:         gsm-1.0-pl10-add-includefile.patch  
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Contains runtime shared libraries for libgsm, an implementation of
the European GSM 06.10 provisional standard for full-rate speech
transcoding, prI-ETS 300 036, which uses RPE/LTP (residual pulse
excitation/long term prediction) coding at 13 kbit/s.

GSM 06.10 compresses frames of 160 13-bit samples (8 kHz sampling
rate, i.e. a frame rate of 50 Hz) into 260 bits; for compatibility
with typical UNIX applications, our implementation turns frames of 160
16-bit linear samples into 33-byte frames (1650 Bytes/s).
The quality of the algorithm is good enough for reliable speaker
recognition; even music often survives transcoding in recognizable 
form (given the bandwidth limitations of 8 kHz sampling rate).

The interfaces offered are a front end modelled after compress(1), and
a library API.  Compression and decompression run faster than realtime
on most SPARCstations.  The implementation has been verified against the
ETSI standard test patterns.

%package -n	%{libname}
Summary:	Shared libraries for GSM speech compressor
Group:          System/Libraries

%description -n	%{libname}
Contains runtime shared libraries for libgsm, an implementation of
the European GSM 06.10 provisional standard for full-rate speech
transcoding, prI-ETS 300 036, which uses RPE/LTP (residual pulse
excitation/long term prediction) coding at 13 kbit/s.

GSM 06.10 compresses frames of 160 13-bit samples (8 kHz sampling
rate, i.e. a frame rate of 50 Hz) into 260 bits; for compatibility
with typical UNIX applications, our implementation turns frames of 160
16-bit linear samples into 33-byte frames (1650 Bytes/s).
The quality of the algorithm is good enough for reliable speaker
recognition; even music often survives transcoding in recognizable 
form (given the bandwidth limitations of 8 kHz sampling rate).

The interfaces offered are a front end modelled after compress(1), and
a library API.  Compression and decompression run faster than realtime
on most SPARCstations.  The implementation has been verified against the
ETSI standard test patterns.

%package -n	%{develname}
Summary:	Development libraries for a GSM speech compressor
Group:		Development/C
Obsoletes:	%mklibname %{name} 1 -d
Provides:	%{name}-devel
Provides:	lib%{name}-devel
Requires:	%{libname} = %{version}-%{release}

%description -n	%{develname}
Contains header files and development libraries for libgsm, an
implementation of the European GSM 06.10 provisional standard for
full-rate speech transcoding, prI-ETS 300 036, which uses RPE/LTP
(residual pulse excitation/long term prediction) coding at 13 kbit/s.

GSM 06.10 compresses frames of 160 13-bit samples (8 kHz sampling
rate, i.e. a frame rate of 50 Hz) into 260 bits; for compatibility
with typical UNIX applications, our implementation turns frames of 160
16-bit linear samples into 33-byte frames (1650 Bytes/s).
The quality of the algorithm is good enough for reliable speaker
recognition; even music often survives transcoding in recognizable 
form (given the bandwidth limitations of 8 kHz sampling rate).

The interfaces offered are a front end modelled after compress(1), and
a library API.  Compression and decompression run faster than realtime
on most SPARCstations.  The implementation has been verified against the
ETSI standard test patterns.

%prep

%setup -q -n %{name}-%{srcver}
%patch0 -p1
%patch1 -p1 -b .includes
%patch3 -p0 -b .shared
%patch4 -p0 -b .add_h_file

%build

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall

ln -snf toast %{buildroot}%{_bindir}/untoast
ln -snf toast %{buildroot}%{_bindir}/tcat

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYRIGHT ChangeLog* README
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/gsm
%{_mandir}/man3/*


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.13-5mdv2011.0
+ Revision: 664929
- mass rebuild

* Wed Feb 09 2011 Jani Välimaa <wally@mandriva.org> 1.0.13-4
+ Revision: 637048
- fix url (mdv#62457)
- fix source

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.13-3mdv2011.0
+ Revision: 605502
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.13-2mdv2010.1
+ Revision: 520115
- rebuilt for 2010.1

* Mon Jun 22 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.13-1mdv2010.0
+ Revision: 387953
- 1.0.13

* Fri Dec 19 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.12-4mdv2009.1
+ Revision: 316207
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0.12-3mdv2009.0
+ Revision: 221104
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 1.0.12-2mdv2008.1
+ Revision: 150238
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Jul 22 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.12-1mdv2008.0
+ Revision: 54450
- new version
- new devel library policy
- drop patch 3
- correct provides/obsoletes


* Tue Jan 16 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1.0.10-13mdv2007.0
+ Revision: 109569
- Update patch4

* Tue Jan 16 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1.0.10-12mdv2007.1
+ Revision: 109509
- Add patch4: Add a .h file (needed by kcall)

* Wed Nov 22 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.10-11mdv2007.1
+ Revision: 86346
- bunzip patches
- Import gsm

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.0.10-10mdk
- Rebuild

* Fri May 06 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.10-9mdk
- rpmlint fixes

* Sun Sep 12 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.0.10-8mdk
- provide a shared lib as well (P3 was taken from dag's package)

* Thu Apr 15 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.0.10-7mdk
- fix missing includes, use correct args to utime()
- build static library with PIC as it is built into a DSO (gstreamer-plugins)


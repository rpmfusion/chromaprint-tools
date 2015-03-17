Name:           chromaprint-tools
Version:        1.1
Release:        1%{?dist}
Summary:        Chromaprint audio fingerprinting tools
Group:          Applications/Multimedia
License:        LGPLv2+
URL:            http://www.acoustid.org/chromaprint/
Source:         https://bitbucket.org/acoustid/chromaprint/downloads/chromaprint-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  fftw-devel >= 3

# examples requires ffmpeg
BuildRequires:  ffmpeg-devel

%description
Chromaprint library is the core component of the AcoustID project. It's a 
client-side library that implements a custom algorithm for extracting 
fingerprints from raw audio sources.

This is a set of Chromaprint tools related to acoustic fingerprinting 
featuring fpcalc an standalone AcoustID tool used by Picard.

%prep
%setup -q -n chromaprint-%{version}


%build
%cmake -DBUILD_EXAMPLES=on -DBUILD_TESTS=off
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# cleaning files managed in the chromaprint main package
rm -f %{buildroot}%{_includedir}/chromaprint.h
rm -f %{buildroot}%{_libdir}/pkgconfig/libchromaprint.pc
rm -f %{buildroot}%{_libdir}/lib*.la
rm -f %{buildroot}%{_libdir}/lib*.so*

%files
%doc COPYING.txt NEWS.txt README.txt
%{_bindir}/fpcalc

%changelog
* Tue Mar 17 2015 Ismael Olea <ismael@olea.org> - 1.1-1   
- update to 1.1
- CHANGES.txt file removed in upstream

* Sun Oct 19 2014 Sérgio Basto <sergio@serjux.com> - 1.0-6
- Rebuilt for FFmpeg 2.4.3

* Fri Sep 26 2014 Nicolas Chauvet <kwizart@gmail.com> - 1.0-5
- Rebuilt for FFmpeg 2.4.x

* Thu Aug 07 2014 Sérgio Basto <sergio@serjux.com> - 1.0-4
- Rebuilt for ffmpeg-2.3

* Sat Mar 29 2014 Sérgio Basto <sergio@serjux.com> - 1.0-3
- Rebuilt for ffmpeg-2.2

* Mon Sep 30 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.0-2
- Rebuilt

* Mon Sep 16 2013 Ismael Olea <ismael@olea.org> - 1.0-1
- update to 1.0

* Thu Aug 15 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.7-6
- Rebuilt for FFmpeg 2.0.x

* Sun May 26 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.7-5
- Rebuilt for x264/FFmpeg

* Sun Apr 28 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.7-4
- https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 24 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.7-3
- Rebuilt for FFmpeg 1.0

* Fri Sep 7 2012 Ismael Olea <ismael@olea.org> - 0.7-2
- bump

* Fri Sep 7 2012 Ismael Olea <ismael@olea.org> - 0.7-1
- update to 0.7

* Tue Jun 26 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.6-6
- Rebuilt for FFmpeg

* Wed May 9 2012 Ismael Olea <ismael@olea.org> - 0.6-5
- bump

* Tue Feb 28 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.6-4
- Rebuilt for x264/FFmpeg

* Sat Jan 14 2012 Ismael Olea <ismael@olea.org> - 0.6-3
- using %cmake macro

* Wed Jan 4 2012 Ismael Olea <ismael@olea.org> - 0.6-2
- minor spec cleaning

* Tue Dec 27 2011 Ismael Olea <ismael@olea.org> - 0.6-1
- update to 0.6
- spec cleaning

* Thu Nov 18 2011 Ismael Olea <ismael@olea.org> - 0.5-2
- first version for RPM-Fusion
- renaming into chromaprint-tools

* Thu Nov 10 2011 Ismael Olea <ismael@olea.org> - 0.5-1
- update to 0.5
- subpackage for fpcalc 

* Sat Aug 06 2011 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.4-1
- Initial package

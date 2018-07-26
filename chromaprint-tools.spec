Name:           chromaprint-tools
Version:        1.4.2
Release:        5%{?dist}
Summary:        Chromaprint audio fingerprinting tools
Group:          Applications/Multimedia
License:        GPLv2+
URL:            http://www.acoustid.org/chromaprint
Source:         https://github.com/acoustid/chromaprint/releases/download/v%{version}/chromaprint-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  fftw-devel >= 3

# examples requires ffmpeg
BuildRequires:  ffmpeg-devel

Obsoletes: picard-freeworld < 1.2
Provides: picard-freeworld = 1.2

%description
Chromaprint library is the core component of the AcoustID project. It's a 
client-side library that implements a custom algorithm for extracting 
fingerprints from raw audio sources.

This is a set of Chromaprint tools related to acoustic fingerprinting 
featuring fpcalc an standalone AcoustID tool used by Picard.

License for binaries is GPLv2+ but source code is MIT + LGPLv2+

%prep
%setup -q -n chromaprint-%{version}


%build
%cmake -DBUILD_EXAMPLES=ON -DBUILD_TESTS=OFF -DCMAKE_BUILD_TYPE=Release -DBUILD_TOOLS=ON
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# cleaning files managed in the chromaprint main package
rm -f %{buildroot}%{_includedir}/chromaprint.h
rm -f %{buildroot}%{_libdir}/pkgconfig/libchromaprint.pc
rm -f %{buildroot}%{_libdir}/lib*.la
rm -f %{buildroot}%{_libdir}/lib*.so*

%files
%doc NEWS.txt README.md
%license LICENSE.md
%{_bindir}/fpcalc

%changelog
* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 08 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.4.2-4
- Rebuilt for new ffmpeg snapshot

* Thu Mar 08 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.4.2-3
- Rebuilt for new ffmpeg snapshot

* Wed Feb 28 2018 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Feb 04 2018 Sérgio Basto <sergio@serjux.com> - 1.4.2-1
- Sync with Fedora proper
- Upstream URL changed to github
- Updating to 1.4.2
- Renamed LICENSE.md
- Binary licenses should be GPLv2+ because linking with fftw (which uses GPLv2+)

* Thu Jan 18 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2-7
- Rebuilt for ffmpeg-3.5 git

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 29 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.2-5
- Rebuild for ffmpeg update

* Sat Mar 18 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jul 30 2016 Julian Sikorski <belegdol@fedoraproject.org> - 1.2-3
- Rebuilt for ffmpeg-3.1.1

* Tue Jul 19 2016 Leigh Scott <leigh123linux@googlemail.com> - 1.2-2
- patch for ffmpeg-3

* Tue Feb 23 2016 Sérgio Basto <sergio@serjux.com> - 1.2-1
- Update to 1.2
- Fix rfbz #2746
- Add license tag.

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

* Fri Nov 18 2011 Ismael Olea <ismael@olea.org> - 0.5-2
- first version for RPM-Fusion
- renaming into chromaprint-tools

* Thu Nov 10 2011 Ismael Olea <ismael@olea.org> - 0.5-1
- update to 0.5
- subpackage for fpcalc 

* Sat Aug 06 2011 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.4-1
- Initial package

Summary:	A powerful batch renamer for KDE
Summary(pl):	Narzêdzie do zmiany nazw plików dla KDE
Name:		krename
Version:	3.0.0
Release:	3
License:	GPL
Group:		X11/Applications
Vendor:		Dominik Seichter <domseichter@web.de>
Source0:	http://dl.sourceforge.net/krename/%{name}-%{version}.tar.bz2
# Source0-md5:	c8e3dc74589bb8a37b2b6635e9d3d78f
Patch0:		%{name}-desktop.patch
URL:		http://krename.sourceforge.net/
BuildRequires:	automake
BuildRequires:	fam-devel
BuildRequires:	kdelibs-devel >= 3.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Krename is a very powerful batch file renamer for KDE3 which can
rename a list of files based on a set of expressions. It can copy/move
the files to another directory or simply rename the input files.
Krename supports many conversion operations, including conversion of a
filename to lowercase or to uppercase, conversion of the first letter
of every word to uppercase, adding numbers to filenames, finding and
replacing parts of the filename, and many more. It can also change
access and modification dates, permissions, and file ownership.

%description -l pl
Krename jest narzêdziem do zmiany nazw plików dla KDE3, które umo¿liwia
zmianê nazw dla listy plików na podstawie zbioru wyra¿eñ. Pozwala
kopiowaæ i/lub przenosiæ pliki do innego katalogu lub po prostu
zmieniaæ nazwy plików. Krename wspiera ró¿ne operacje konwersji,
miêdzy innymi konwersjê nazw plików do ma³ych lub do wielkich liter,
konwersjê pierwszej litery ka¿dego s³owa do wielkiej litery, dodanie
numeru do nazwy pliku, zmianê konkretnej czê¶ci nazwy pliku i inne.
Program pozwala równie¿ na zmianê daty dostêpu i modyfikacji,
uprawnieñ oraz w³asno¶ci plików.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub admin
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
%configure \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{zh_TW.Big5,zh_TW}

install -d $RPM_BUILD_ROOT%{_desktopdir}
mv -f $RPM_BUILD_ROOT%{_datadir}/applnk/Utilities/krename.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_datadir}/apps/krename
%{_datadir}/apps/konqueror/servicemenus/*.desktop
%{_iconsdir}/hicolor/*/apps/*.png

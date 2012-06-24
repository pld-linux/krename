Summary:	A powerful batch renamer for KDE
Summary(pl):	Narz�dzie do zmiany nazw plik�w dla KDE
Name:		krename
Version:	3.0.7
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/krename/%{name}-%{version}.tar.bz2
# Source0-md5:	8896375266cfb9249aafd15d117cc11b
Patch0:		%{name}-desktop.patch
URL:		http://www.krename.net/
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
Krename jest narz�dziem do zmiany nazw plik�w dla KDE3, kt�re umo�liwia
zmian� nazw dla listy plik�w na podstawie zbioru wyra�e�. Pozwala
kopiowa� i/lub przenosi� pliki do innego katalogu lub po prostu
zmienia� nazwy plik�w. Krename wspiera r�ne operacje konwersji,
mi�dzy innymi konwersj� nazw plik�w do ma�ych lub do wielkich liter,
konwersj� pierwszej litery ka�dego s�owa do wielkiej litery, dodanie
numeru do nazwy pliku, zmian� konkretnej cz�ci nazwy pliku i inne.
Program pozwala r�wnie� na zmian� daty dost�pu i modyfikacji,
uprawnie� oraz w�asno�ci plik�w.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub admin
%configure \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT	\
	kde_htmldir=%{_kdedocdir}

mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{zh_TW.Big5,zh_TW}
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{zh_CN.GB2312,zh_CN}

install -d $RPM_BUILD_ROOT%{_desktopdir}/kde
mv -f $RPM_BUILD_ROOT%{_datadir}/applnk/Utilities/krename.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}/kde

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/kde/*.desktop
%{_datadir}/apps/krename
%{_datadir}/apps/konqueror/servicemenus/*.desktop
%{_iconsdir}/hicolor/*/apps/*.png

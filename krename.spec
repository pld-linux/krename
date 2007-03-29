Summary:	A powerful batch renamer for KDE
Summary(pl.UTF-8):	Narzędzie do zmiany nazw plików dla KDE
Name:		krename
Version:	3.0.13
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/krename/%{name}-%{version}.tar.bz2
# Source0-md5:	93b4a74d0ef67213a5947dc5fb10b9cf
Source1:	http://dl.sourceforge.net/krename/%{name}-3.0.3.pdf
# Source1-md5:	0e598b7acf88e80bf76fdfd22d8c7929
Patch0:		%{name}-desktop.patch
URL:		http://www.krename.net/
BuildRequires:	automake
BuildRequires:	fam-devel
BuildRequires:	kdelibs-devel >= 9:3.0
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

%description -l pl.UTF-8
Krename jest narzędziem do zmiany nazw plików dla KDE3, które umożliwia
zmianę nazw dla listy plików na podstawie zbioru wyrażeń. Pozwala
kopiować i/lub przenosić pliki do innego katalogu lub po prostu
zmieniać nazwy plików. Krename wspiera różne operacje konwersji,
między innymi konwersję nazw plików do małych lub do wielkich liter,
konwersję pierwszej litery każdego słowa do wielkiej litery, dodanie
numeru do nazwy pliku, zmianę konkretnej części nazwy pliku i inne.
Program pozwala również na zmianę daty dostępu i modyfikacji,
uprawnień oraz własności plików.

%package doc
Summary:	Krename documentation
Summary(pl.UTF-8):	Dokumentacja programu Krename
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description doc
Documentation for Krename in PDF format.

%description doc -l pl.UTF-8
Dokumentacja do Krename w formacie PDF.

%prep
%setup -q
cp %{SOURCE1} .
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
rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

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

%files doc
%defattr(644,root,root,755)
%doc krename-3.0.3.pdf

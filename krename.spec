
%define		_ver	3.0.14
%define		_pdf_ver	3.0.12

Summary:	A powerful batch renamer for KDE
Summary(pl.UTF-8):	Narzędzie do zmiany nazw plików dla KDE
Name:		krename
Version:	%{_ver}
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/krename/%{name}-%{version}.tar.bz2
# Source0-md5:	1f5fe57384d912c11fbd0fae94bb7fca
Source1:	http://dl.sourceforge.net/krename/%{name}-%{_pdf_ver}.pdf
# Source1-md5:	98141b57a29984af265aeecfd7ea8b93
Patch0:		%{name}-desktop.patch
URL:		http://www.krename.net/
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
%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
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

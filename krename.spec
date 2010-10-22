
%define		_pdf_ver	3.0.12

Summary:	A powerful batch renamer for KDE
Summary(pl.UTF-8):	Narzędzie do zmiany nazw plików dla KDE
Name:		krename
Version:	4.0.5
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/krename/%{name}-%{version}.tar.bz2
# Source0-md5:	3e064cadc6fb6f6e269ed914fb00995a
Source1:	http://dl.sourceforge.net/krename/%{name}-%{_pdf_ver}.pdf
# Source1-md5:	98141b57a29984af265aeecfd7ea8b93
Patch0:		%{name}-desktop.patch
URL:		http://www.krename.net/
BuildRequires:	QtNetwork-devel
BuildRequires:	QtSvg-devel
BuildRequires:	automoc4
BuildRequires:	cmake
BuildRequires:	exiv2-devel
BuildRequires:	fam-devel
BuildRequires:	gettext-devel
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	pkgconfig
BuildRequires:	podofo-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	taglib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Krename is a very powerful batch file renamer for KDE which can rename
a list of files based on a set of expressions. It can copy/move the
files to another directory or simply rename the input files. Krename
supports many conversion operations, including conversion of a
filename to lowercase or to uppercase, conversion of the first letter
of every word to uppercase, adding numbers to filenames, finding and
replacing parts of the filename, and many more. It can also change
access and modification dates, permissions, and file ownership.

%description -l pl.UTF-8
Krename jest narzędziem do zmiany nazw plików dla KDE, które umożliwia
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
install -d build
cd build
%cmake \
		-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" == "lib64"
		-DLIB_SUFFIX=64 \
%endif
		../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/krename
%{_desktopdir}/kde4/krename.desktop
%{_iconsdir}/hicolor/*x*/apps/krename.png
%{_datadir}/kde4/services/ServiceMenus/krename_all_nonrec.desktop
%{_datadir}/kde4/services/ServiceMenus/krename_dir_rec.desktop

%files doc
%defattr(644,root,root,755)
%doc %{name}-%{_pdf_ver}.pdf

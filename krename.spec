Summary:	A powerfull batch renamer for KDE
Summary(pl):	Narzêdzie do zmiany nazw plików dla KDE
Name:		krename
Version:	2.5.4
Release:	1
License:	GPL
Vendor:		Dominik Seichter <domseichter@web.de>
Url:		http://krename.sourceforge.net/
Source0:	http://telia.dl.sourceforge.net/sourceforge/krename/%{name}-%{version}.tar.bz2
Group:		X11/Applications
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:  kdelibs-devel >= 3.0
BuildRequires:  fam-devel

%define		_htmldir	/usr/share/doc/kde/HTML

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
zmianê nazw dla listy plików na podstawie zbioru wyra¿eñ. Pozwala kopiowaæ
i/lub przenosiæ pliki do innego katalogu lub po prostu zmieniaæ nazwy plików.
Krename wspiera ró¿ne operacje konwersji, miêdzy innymi konwersjê nazw plików
do ma³ych lub do wielkich liter, konwersjê pierwszej litery ka¿dego s³owa
do wielkiej litery, dodanie numeru do nazwy pliku, zmianê konkretnej czê¶ci
nazwy pliku i inne. Program pozwala równie¿ na zmianê daty dostêpu i modyfikacji,
uprawnieñ oraz w³asno¶ci plików.

%prep
%setup -q

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
%configure

# Setup for parallel builds
numprocs=`egrep -c ^cpu[0-9]+ /proc/stat || :`
if [ "$numprocs" = "0" ]; then
  numprocs=1
fi

%{__make} -j$numprocs

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install-strip DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Utilities/*
%{_datadir}/apps/*
%{_pixmapsdir}/*/*/*/*

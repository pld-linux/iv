Summary:	ImgView - simple GTK+ image viewer using Imlib
Summary(pl.UTF-8):	ImgView - prosta przeglądarka obrazków oparta na GTK+ i używająca Imliba
Name:		iv
Version:	2.6.1
Release:	4
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	http://wolfsinger.com/~wolfpack/packages/%{name}-%{version}.tar.bz2
# Source0-md5:	e18ffd722be6905e69c97d641b5c6839
Patch0:		%{name}-vidmode.patch
Patch1:		%{name}-libpng.patch
Patch2:		%{name}-verbose.patch
URL:		http://freecode.com/projects/iv
BuildRequires:	gtk+-devel
BuildRequires:	imlib-devel
BuildRequires:	libpng-devel >= 2:1.4.0
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple GTK+ image viewer using Imlib.

%description -l pl.UTF-8
Prosta przeglądarka obrazków oparta na GTK+ i używająca Imliba.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
./configure Linux
%{__make} -C iv \
	CC="%{__cc}" \
	CPP="%{__cxx}" \
	CFLAGS="%{rpmcflags} %{!?debug:-fomit-frame-pointer} -ffast-math -Wall \
		-DHAVE_LIBPNG -DHAVE_IMLIB -DINCLUDE_IV_TITLE_IMAGE \
		`gtk-config --cflags` `imlib-config --cflags`"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install -C iv \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	ICONS_DIR=$RPM_BUILD_ROOT%{_pixmapsdir} \
	MAN_DIR=$RPM_BUILD_ROOT%{_mandir}/man1

bzip2 -d $RPM_BUILD_ROOT%{_mandir}/man1/*.bz2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/iv
%{_pixmapsdir}/iv.xpm
%{_mandir}/man1/iv.1*

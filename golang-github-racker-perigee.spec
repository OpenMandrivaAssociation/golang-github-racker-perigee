# http://github.com/racker/perigee

%global goipath         github.com/racker/perigee
%global commit          0c00cb0a026b71034ebc8205263c77dad3577db5


%gometa -i

Name:           %{goname}
Version:        0
Release:        0.12%{?dist}
Summary:        REST client optimized for use with APIs for request and response bodies
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml
Patch0:         Fix-formatting.patch

%description
Perigee provides a REST client that, while it should be generic enough
to use with most any RESTful API, is nonetheless optimized to the needs
of the OpenStack APIs. Perigee grew out of the need to refactor out
common API access code from the gorax project.

Several things influenced the name of the project. Numerous elements
of the OpenStack ecosystem are named after astronomical artifacts.
Additionally, perigee occurs when two orbiting bodies are closest
to each other. Perigee seemed appropriate for something aiming to bring
OpenStack and other RESTful services closer to the end-user.

This library is still in the very early stages of development.

%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
Perigee provides a REST client that, while it should be generic enough
to use with most any RESTful API, is nonetheless optimized to the needs
of the OpenStack APIs. Perigee grew out of the need to refactor out
common API access code from the gorax project.

Several things influenced the name of the project. Numerous elements 
of the OpenStack ecosystem are named after astronomical artifacts. 
Additionally, perigee occurs when two orbiting bodies are closest 
to each other. Perigee seemed appropriate for something aiming to bring 
OpenStack and other RESTful services closer to the end-user.

This library is still in the very early stages of development.

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .
%patch0 -p1

%install
%goinstall glide.lock glide.yaml

%check
%gochecks -d .

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.11.git0c00cb0
- Upload glide files

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.git0c00cb0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.git0c00cb0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.git0c00cb0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.git0c00cb0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.git0c00cb0
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.git0c00cb0
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.git0c00cb0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Aug 07 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.3.git0c00cb0
- Update spec file to spec-2.0
  resolves: #1250497

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.git0c00cb0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct 16 2014 jchaloup <jchaloup@redhat.com> - 0-0.1.git0c00cb0
- First package for Fedora
  resolves: #1153726


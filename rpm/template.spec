%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-examples-tf2-py
Version:        0.33.2
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS examples_tf2_py package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-rolling-geometry-msgs
Requires:       ros-rolling-launch-ros
Requires:       ros-rolling-rclpy
Requires:       ros-rolling-sensor-msgs
Requires:       ros-rolling-tf2-ros-py
Requires:       ros-rolling-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-rolling-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  ros-rolling-ament-copyright
BuildRequires:  ros-rolling-ament-flake8
BuildRequires:  ros-rolling-ament-pep257
%endif

%description
Has examples of using the tf2 Python API.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/rolling"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Wed Oct 04 2023 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 0.33.2-1
- Autogenerated by Bloom

* Thu Sep 07 2023 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 0.33.1-1
- Autogenerated by Bloom

* Mon Aug 21 2023 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 0.33.0-1
- Autogenerated by Bloom

* Tue Jul 11 2023 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 0.32.2-1
- Autogenerated by Bloom

* Thu May 11 2023 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 0.32.1-1
- Autogenerated by Bloom

* Thu Apr 27 2023 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 0.32.0-1
- Autogenerated by Bloom

* Thu Apr 13 2023 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 0.31.2-1
- Autogenerated by Bloom

* Wed Apr 12 2023 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 0.31.1-1
- Autogenerated by Bloom

* Tue Apr 11 2023 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 0.31.0-1
- Autogenerated by Bloom

* Tue Mar 21 2023 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 0.30.0-3
- Autogenerated by Bloom


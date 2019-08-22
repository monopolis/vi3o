v0.9.0
------
* Added :py:class:`vi3o.recording.Recording` for reading AXIS NAS/SD-card recordings.
* Fixed segfault when requesting grey encoding.
* Fixed library compatibility with :mod:`pathlib`.
* Fixed compatibility for Pyglet 1.4.
* Fixed pinning of dependencies to Python 2.7 compatible versions.
* Fixed segfault when requesting gray video.
* Fixed timestamps property of frames from :py:class:`vi3o.cat.VideoCat` to be relative to first frame in first video.


v0.8.0
------
* Silence some compiler warnings
* Added reindex parameter to :class:`vi3o.mkv.Mkv`
* Support for sliced views of :class:`vi3o.opencv.CvVideo`
* Support for mkv files with both keyframe and user data frame in the same matrosca frame
* Support for negative timecodes in mkv streams
* Use imageio as default fallback video decoder instead as opencv is missbehaving
* Silence deprication warning
* Removed deprecated pixel format warning on Ubuntu Xenial
* Bumped index version number to eusure indexes are recreated with above bugfixes


v0.7.4
------
* Remove numpy as dependency to setup.py
* Fixed dependencies for setuptools test command
* Removed deprecated pixel format warning
* Added script to run unit tests localy in docker

v0.7.3
------
* Support for random access in mjpeg coded .mkv files.

v0.7.2
------
* Support for .mkv files with mjpg codec. Timestamps are in this case red from jpg-headers
  so there is no need for user-data packages in the mkv stream.
* Passing grey=True to :class:`vi3o.mjpg.Mjpg` no longer results in segfault.

v0.7.0
------
* Added :py:func:`vi3o.mjpg.jpg_info` for reading Axis user data from single images.
* Added :py:func:`vi3o.image.imrotate_and_scale`
* :py:func:`vi3o.image.imread` now raises IoError when failing to load an image with repair=False
* :py:func:`vi3o.image.imread` will now by default warn if it tried to load a broken image
* :class:`vi3o.opencv.CvVideo` now supports greyscale video
* :class:`vi3o.netcam.AxisCam` now uses digest authentication instead of basic
* Added a parameter to :class:`vi3o.netcam.AxisCam` to make it ignore proxy setting
* Added support for general vapix parameters in :class:`vi3o.netcam.AxisCam`
* Support for avi and mp4 files in :mod:`vi3o.debugview`
* Improved backwards compatibility with opencv
* Made class:`vi3o.mkv.Mkv` objects picklable


v0.6.1
------
* Setup now depends on numpy
* No longer depends on cv2.cv.FOURCC, which has been droppen in recent opencv version
* Recognize upper case filename extntions
* Select betwen av_frame_alloc and avcodec_alloc_frame based on libav version

v0.6.0
------
* Added properties :py:attr:`vi3o.mjpg.Mjpg.hwid`, :py:attr:`vi3o.mjpg.Mjpg.serial_number`, :py:attr:`vi3o.mjpg.Mjpg.firmware_version`.
* Added *repair* option to :py:func:`vi3o.image.imread`.
* Added :class:`vi3o.VideoCat` and :class:`vi3o.VideoGlob`
* Fixed buggy *systimes* property on sliced Mkv *Video* objects
* Support *Video* objects as input argument to :class:`vi3o.SyncedVideos`
* Added :class:`vi3o.opencv.CvOut`
* Added :py:func:`vi3o.image.imload` and :py:func:`vi3o.image.imwrite` aliases

v0.5.2
------
* Slightly lighter background color behind images in DebugView to distinguish black backgrounds from outside image.
* Support for reading system timestamps from more recnt Axis cameras.
* Added a OpenCV fallback to allow unknown video formats to handled as `Video` object even if there are no system timestamps.
* Fixed a segfault when parsing broken or truncated mkv files.

v0.5.0
------
* Added :class:`vi3o.netcam.AxisCam` for reading video directly from Axis camera
* Add systimes property to Mkv and SyncedVideos to get a list of all system timestamps without decoding the frames.
* Switch to setuptools for proper handing of cffi dependency
* Remove numpy dependency during setup
* Dont try to decode truncated mkv frames

v0.4.0
------

* Allow negative indexes to wrap around in `Video` objects.
* Added :class:`vi3o.SyncedVideos` for syncornizing videos using `systime`.
* Support for showing images of different size side by side in the debug viewer.
* Support for showing images of different size one after the other in the debug viewer.
* Move the generated .idx files to the user .cache dir
* Regenerate the .idx files if the video is modfied
* Added :py:func:`vi3o.image.imrotate`.
* Added :py:func:`vi3o.image.imshow`.
* Added support for greyscale mjpg files.
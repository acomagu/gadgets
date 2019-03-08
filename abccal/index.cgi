#!/usr/bin/env bash
echo 'Content-Type: text/calendar'
echo
curl https://calendar.google.com/calendar/ical/atcoder.jp_gqd1dqpjbld3mhfm4q07e4rops%40group.calendar.google.com/public/basic.ics \
  | sed -e '/BEGIN:VEVENT/{:l N; /END:VEVENT/!bl; /\(Beginner\|ABC\)/!d;}'

#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from gmail_new_thread_trigger.crew import GmailNewThreadTrigger

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information


def run():
    """
    Run the crew.
    """
    # Example Gmail message inputs - replace with actual message ID and recipient email from Gmail trigger
    # The message_id should be the Gmail message ID to retrieve
    inputs = {
        "crewai_trigger_payload": '''
{
  "result": {
    "id": "198adefd9068d7bc",
    "threadId": "198adefd9068d7bc",
    "labelIds": [
      "UNREAD",
      "CATEGORY_UPDATES",
      "INBOX"
    ],
    "snippet": "Deployment Successful! 🎉 Hi lucas, Your crew / flow has been successfully deployed and is now live! Deployment Name: crewai-gmail-new-thread-trigger API URL: https://crewai-gmail-new-thread-trigger-",
    "payload": {
      "partId": "",
      "mimeType": "multipart/alternative",
      "filename": "",
      "headers": [
        {
          "name": "Delivered-To",
          "value": "lucas@crewai.com"
        },
        {
          "name": "Received",
          "value": "by 2002:a05:7010:61cc:b0:485:319f:48f7 with SMTP id y12csp2488595mdc;        Fri, 15 Aug 2025 06:33:54 -0700 (PDT)"
        },
        {
          "name": "X-Google-Smtp-Source",
          "value": "AGHT+IGeNmrfk2Fz/S+RsU2/sXfNiZZZ6Qdf2dP9nc7ePCbq5sMiC+l+HgUqgR7fRWlCYfP5EUX7"
        },
        {
          "name": "X-Received",
          "value": "by 2002:a05:620a:708c:b0:7e6:8bc0:361d with SMTP id af79cd13be357-7e87df88a45mr146580085a.4.1755264833609;        Fri, 15 Aug 2025 06:33:53 -0700 (PDT)"
        },
        {
          "name": "ARC-Seal",
          "value": "i=1; a=rsa-sha256; t=1755264833; cv=none;        d=google.com; s=arc-20240605;        b=iJcy/jMdwZm9MRIX3kIX0j8YLlXYifaQ1+unmxxUKSZq9LhVKbqP5RNrfIsqlB7fmB         DtDcMj4jduVsMJgfXY88wbGlq/WlZDqZMSqeFzCNctj8whC6PlH9fy1CjjwkXb4Q11BF         I7rdx1RsBn50wCJ3zwfvCAp5ZlGDb37KaeEz/z2EQT64Y/2D9YCF0yO82poYQK8di2w+         qvoM27h7Orgx8uSi8HiG2GJx/uxpcY0KVxJUaBdyA4Law3g2tQu08LUvTZ2gUjLeVMr5         IpuYq8CJ53kd/aGDOO+cws6Fvd0XmVUKlI6VuLvMKSg2uU68pUohQb6APzhHhjPHiNxg         Sxcg=="
        },
        {
          "name": "ARC-Message-Signature",
          "value": "i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20240605;        h=feedback-id:mime-version:date:message-id:subject:to:from         :dkim-signature:dkim-signature;        bh=O2QMkqe1aFEQhJBVpP8XWH5tWUvqW1pqwk0b6hwDah0=;        fh=tFPPtf98w6bKBdG60uonrSdbvvVAs+stj9+UxBL8zGs=;        b=ZLznnUSgzQCSVODavklA7Q+7YV2G8eDJyl+JbC89zX0ALmm4W5vpwC3XM3mWgBgjz3         gJ6Fn/r2UZdrkV53BJT1WcooPKZzbpF8rsOV+RwbNT5coAVYSStduisqWQuZgmp6q+HK         niWSvYabVHSuTMBT2sNmqa7LDTWw9vvXVPc7PCFKWjPl9BMpDH8u3Kb74g0pfzNHyXNT         BzEYdvTRHZ/RCLOg4h9o7pmkHDa+4KRVLmMSyXfe5VYjexAuGbSTyKyd1mB2v7/qhqov         ob0MwROluMaCVkGWyUpU/7VpLtG7A40LEKXpLpTl+6HPlqdd+f1qrdLZeuJ2WsemBdzk         hdXg==;        dara=google.com"
        },
        {
          "name": "ARC-Authentication-Results",
          "value": "i=1; mx.google.com;       dkim=pass header.i=@crewai.com header.s=resend header.b=dFjM68Co;       dkim=pass header.i=@amazonses.com header.s=6gbrjpgwjskckoa6a5zn6fwqkn67xbtw header.b=\"IMlVNV/5\";       spf=pass (google.com: domain of 01000198adefd5f5-b11d9240-9165-4eab-9e68-be29dfc02d45-000000@send.crewai.com designates 54.240.9.1 as permitted sender) smtp.mailfrom=01000198adefd5f5-b11d9240-9165-4eab-9e68-be29dfc02d45-000000@send.crewai.com;       dmarc=pass (p=QUARANTINE sp=QUARANTINE dis=NONE) header.from=crewai.com"
        },
        {
          "name": "Return-Path",
          "value": "<01000198adefd5f5-b11d9240-9165-4eab-9e68-be29dfc02d45-000000@send.crewai.com>"
        },
        {
          "name": "Received",
          "value": "from a9-1.smtp-out.amazonses.com (a9-1.smtp-out.amazonses.com. [54.240.9.1])        by mx.google.com with ESMTPS id d75a77b69052e-4b11de71bc8si5753551cf.607.2025.08.15.06.33.53        for <lucas@crewai.com>        (version=TLS1_3 cipher=TLS_AES_128_GCM_SHA256 bits=128/128);        Fri, 15 Aug 2025 06:33:53 -0700 (PDT)"
        },
        {
          "name": "Received-SPF",
          "value": "pass (google.com: domain of 01000198adefd5f5-b11d9240-9165-4eab-9e68-be29dfc02d45-000000@send.crewai.com designates 54.240.9.1 as permitted sender) client-ip=54.240.9.1;"
        },
        {
          "name": "Authentication-Results",
          "value": "mx.google.com;       dkim=pass header.i=@crewai.com header.s=resend header.b=dFjM68Co;       dkim=pass header.i=@amazonses.com header.s=6gbrjpgwjskckoa6a5zn6fwqkn67xbtw header.b=\"IMlVNV/5\";       spf=pass (google.com: domain of 01000198adefd5f5-b11d9240-9165-4eab-9e68-be29dfc02d45-000000@send.crewai.com designates 54.240.9.1 as permitted sender) smtp.mailfrom=01000198adefd5f5-b11d9240-9165-4eab-9e68-be29dfc02d45-000000@send.crewai.com;       dmarc=pass (p=QUARANTINE sp=QUARANTINE dis=NONE) header.from=crewai.com"
        },
        {
          "name": "DKIM-Signature",
          "value": "v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple; s=resend; d=crewai.com; t=1755264833; h=From:To:Subject:Message-ID:Date:MIME-Version:Content-Type; bh=MxdLt/ss011HslUdM12PiUJCMWUXbWAVb3rRUs9mSDk=; b=dFjM68CoxouF66r88vmFttbn/gfkwAUKVBm44PaNSXNFhh+GHEDDd+hBw3Xc0Mhj dnccYFssT0/SfkfQbcjR1aMB3vni+ZGUKnmj7lh33X0P1EwmDXdpLP1gZQA7yq3Hd8e cTQNyUfj3M/F7Jr6z38po/xBU6nJEnho7q737mkQ="
        },
        {
          "name": "DKIM-Signature",
          "value": "v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple; s=6gbrjpgwjskckoa6a5zn6fwqkn67xbtw; d=amazonses.com; t=1755264833; h=From:To:Subject:Message-ID:Date:MIME-Version:Content-Type:Feedback-ID; bh=MxdLt/ss011HslUdM12PiUJCMWUXbWAVb3rRUs9mSDk=; b=IMlVNV/5cgmRp6cmx5Z+FU0ki/ly5/6QqtaJQKA3+GrsyP38sExezEztk7l1EqP2 4ARfHKWFp5ZbY+0+8c7vZRqbGmfLAd7wEJAR7eEoYJ9fpljk6fpEuVsJ/cwjARE5tco np52fRz7EEAUBOMtDJyq/ZJX0LOhmc3OB+li+5Dk="
        },
        {
          "name": "From",
          "value": "donotreply@crewai.com"
        },
        {
          "name": "To",
          "value": "lucas@crewai.com"
        },
        {
          "name": "Subject",
          "value": "Deployment Success"
        },
        {
          "name": "Message-ID",
          "value": "<01000198adefd5f5-b11d9240-9165-4eab-9e68-be29dfc02d45-000000@email.amazonses.com>"
        },
        {
          "name": "Date",
          "value": "Fri, 15 Aug 2025 13:33:53 +0000"
        },
        {
          "name": "MIME-Version",
          "value": "1.0"
        },
        {
          "name": "Content-Type",
          "value": "multipart/alternative; boundary=\"--_NmP-b9d2cde4dc65f9b0-Part_1\""
        }
      ],
      "body": {
        "size": 0
      },
      "parts": [
        {
          "partId": "0",
          "mimeType": "text/plain",
          "filename": "",
          "headers": [
            {
              "name": "Content-Type",
              "value": "text/plain; charset=utf-8"
            },
            {
              "name": "Content-Transfer-Encoding",
              "value": "quoted-printable"
            }
          ],
          "body": {
            "size": 774,
            "data": "REVQTE9ZTUVOVCBTVUNDRVNTRlVMISDwn46JDQoNCkhpIGx1Y2FzLA0KWW91ciBjcmV3IC8gZmxvdyBoYXMgYmVlbiBzdWNjZXNzZnVsbHkgZGVwbG95ZWQgYW5kIGlzIG5vdyBsaXZlIQ0KDQpEZXBsb3ltZW50IE5hbWU6IGNyZXdhaS1nbWFpbC1uZXctdGhyZWFkLXRyaWdnZXIgQVBJIFVSTDoNCmh0dHBzOi8vY3Jld2FpLWdtYWlsLW5ldy10aHJlYWQtdHJpZ2dlci1hZmRjZWJlYi0yYy1lZmU1ZjU2ZS5jcmV3YWkuY29tIEJlYXJlcg0KVG9rZW46IDIxOGViMjU2YTllMQ0KDQpZb3VyIGNyZXcgaXMgbm93IGF2YWlsYWJsZSBhcyBhbiBBUEkuIEhlcmUncyBob3cgdG8gdXNlIGl0Og0KDQogMS4gR2V0IHJlcXVpcmVkIGlucHV0czoNCiAgICBHRVQgL2lucHV0cw0KIDIuIFN0YXJ0IHlvdXIgY3JldzoNCiAgICBQT1NUIC9raWNrb2ZmDQogMy4gQ2hlY2sgZXhlY3V0aW9uIHN0YXR1czoNCiAgICBHRVQgL3N0YXR1cy97dGFza19pZH0NCg0KUmVtZW1iZXIgdG8gaW5jbHVkZSB5b3VyIGJlYXJlciB0b2tlbiBpbiB0aGUgYXV0aG9yaXphdGlvbiBoZWFkZXIgZm9yIGFsbA0KcmVxdWVzdHMuDQoNClZpZXcgRGVwbG95bWVudCBodHRwczovL2FwcC5jcmV3YWkuY29tL2NyZXdhaV9wbHVzL2RlcGxveW1lbnRzLzEwMzQ4Mg0KDQpGb3IgZGV0YWlsZWQgQVBJIGRvY3VtZW50YXRpb24sIHZpc2l0IG91ciBBUEkgZ3VpZGUNCmh0dHBzOi8vaGVscC5jcmV3YWkuY29tL3VzaW5nLXlvdXItY3Jld3MtYXBpLWluLWNyZXdhaS4NCg0KVGhhbmsgeW91LA0KU3VwcG9ydCBUZWFt"
          }
        },
        {
          "partId": "1",
          "mimeType": "text/html",
          "filename": "",
          "headers": [
            {
              "name": "Content-Type",
              "value": "text/html; charset=utf-8"
            },
            {
              "name": "Content-Transfer-Encoding",
              "value": "quoted-printable"
            }
          ],
          "body": {
            "size": 5066,
            "data": "PCFET0NUWVBFIGh0bWw-DQo8aHRtbD4NCiAgPGhlYWQ-DQogICAgPG1ldGEgaHR0cC1lcXVpdj0iQ29udGVudC1UeXBlIiBjb250ZW50PSJ0ZXh0L2h0bWw7IGNoYXJzZXQ9dXRmLTgiPg0KICAgIDxzdHlsZT4NCiAgICAgIC8qIEVtYWlsIHN0eWxlcyBuZWVkIHRvIGJlIGlubGluZSAqLw0KICAgIDwvc3R5bGU-DQogIDwvaGVhZD4NCg0KICA8Ym9keT4NCiAgICA8dGFibGUNCiAgY2VsbHBhZGRpbmc9IjAiDQogIGNlbGxzcGFjaW5nPSIwIg0KICBib3JkZXI9IjAiDQogIHdpZHRoPSIxMDAlIg0KICBzdHlsZT0iZm9udC1mYW1pbHk6ICdBcmlhbCcsIHNhbnMtc2VyaWY7Ig0KPg0KICA8dHI-DQogICAgPHRkIGFsaWduPSJjZW50ZXIiIHN0eWxlPSJwYWRkaW5nOiAwIDQwcHg7Ij4NCiAgICAgIDx0YWJsZQ0KICAgICAgICBjZWxscGFkZGluZz0iMCINCiAgICAgICAgY2VsbHNwYWNpbmc9IjAiDQogICAgICAgIGJvcmRlcj0iMCINCiAgICAgICAgd2lkdGg9IjEwMCUiDQogICAgICAgIHN0eWxlPSJtYXgtd2lkdGg6IDYwMHB4OyBib3JkZXI6IDFweCBzb2xpZCBsaWdodGdyYXk7IGJvcmRlci1yYWRpdXM6IDEycHg7Ig0KICAgICAgPg0KICAgICAgICA8dHI-DQogICAgICAgICAgPHRkIGFsaWduPSJjZW50ZXIiIHN0eWxlPSJwYWRkaW5nOiA0MHB4OyI-DQogICAgICAgICAgICA8aDMgc3R5bGU9ImNvbG9yOiAjMzMzOyBtYXJnaW4tdG9wOiAwOyI-RGVwbG95bWVudCBTdWNjZXNzZnVsISDwn46JPC9oMz4NCg0KICAgICAgICAgICAgPHRhYmxlIGNlbGxwYWRkaW5nPSIwIiBjZWxsc3BhY2luZz0iMCIgYm9yZGVyPSIwIiB3aWR0aD0iMTAwJSI-DQogICAgICAgICAgICAgIDx0cj4NCiAgICAgICAgICAgICAgICA8dGQgc3R5bGU9InBhZGRpbmctYm90dG9tOiAyMHB4OyI-DQogICAgICAgICAgICAgICAgICA8ZGl2IHN0eWxlPSJ0ZXh0LXRyYW5zZm9ybTogY2FwaXRhbGl6ZTsgbWFyZ2luOiAwOyI-SGkNCiAgICAgICAgICAgICAgICAgICAgbHVjYXMsPC9kaXY-DQogICAgICAgICAgICAgICAgICA8ZGl2IHN0eWxlPSJtYXJnaW46IDEwcHggMCAwIDA7Ij5Zb3VyIGNyZXcgLyBmbG93IGhhcyBiZWVuIHN1Y2Nlc3NmdWxseSBkZXBsb3llZCBhbmQgaXMgbm93IGxpdmUhPC9kaXY-DQogICAgICAgICAgICAgICAgPC90ZD4NCiAgICAgICAgICAgICAgPC90cj4NCiAgICAgICAgICAgIDwvdGFibGU-DQoNCiAgICAgICAgICAgIDx0YWJsZSBjZWxscGFkZGluZz0iMCIgY2VsbHNwYWNpbmc9IjAiIGJvcmRlcj0iMCIgd2lkdGg9IjEwMCUiPg0KICAgICAgICAgICAgICA8dHI-DQogICAgICAgICAgICAgICAgPHRkIHN0eWxlPSJwYWRkaW5nLWJvdHRvbTogMTBweDsiPg0KICAgICAgICAgICAgICAgICAgPHN0cm9uZz5EZXBsb3ltZW50IE5hbWU6PC9zdHJvbmc-DQogICAgICAgICAgICAgICAgICBjcmV3YWktZ21haWwtbmV3LXRocmVhZC10cmlnZ2VyDQogICAgICAgICAgICAgICAgPC90ZD4NCiAgICAgICAgICAgICAgPC90cj4NCiAgICAgICAgICAgICAgPHRyPg0KICAgICAgICAgICAgICAgIDx0ZCBzdHlsZT0icGFkZGluZy1ib3R0b206IDEwcHg7Ij4NCiAgICAgICAgICAgICAgICAgIDxzdHJvbmc-QVBJIFVSTDo8L3N0cm9uZz4NCiAgICAgICAgICAgICAgICAgIGh0dHBzOi8vY3Jld2FpLWdtYWlsLW5ldy10aHJlYWQtdHJpZ2dlci1hZmRjZWJlYi0yYy1lZmU1ZjU2ZS5jcmV3YWkuY29tDQogICAgICAgICAgICAgICAgPC90ZD4NCiAgICAgICAgICAgICAgPC90cj4NCiAgICAgICAgICAgICAgPHRyPg0KICAgICAgICAgICAgICAgIDx0ZCBzdHlsZT0icGFkZGluZy1ib3R0b206IDEwcHg7Ij4NCiAgICAgICAgICAgICAgICAgIDxzdHJvbmc-QmVhcmVyIFRva2VuOjwvc3Ryb25nPg0KICAgICAgICAgICAgICAgICAgMjE4ZWIyNTZhOWUxDQogICAgICAgICAgICAgICAgPC90ZD4NCiAgICAgICAgICAgICAgPC90cj4NCiAgICAgICAgICAgICAgPHRyPg0KICAgICAgICAgICAgICAgIDx0ZCBzdHlsZT0icGFkZGluZy1ib3R0b206IDIwcHg7Ij4NCiAgICAgICAgICAgICAgICAgIDxwIHN0eWxlPSJtYXJnaW46IDAgMCAxMHB4IDA7Ij5Zb3VyIGNyZXcgaXMgbm93IGF2YWlsYWJsZSBhcyBhbiBBUEkuIEhlcmUncyBob3cgdG8gdXNlIGl0OjwvcD4NCiAgICAgICAgICAgICAgICAgIDxvbCBzdHlsZT0ibWFyZ2luOiAwIDAgMTBweCAyMHB4OyBwYWRkaW5nOiAwOyI-DQogICAgICAgICAgICAgICAgICAgIDxsaSBzdHlsZT0ibWFyZ2luLWJvdHRvbTogMTBweDsiPkdldCByZXF1aXJlZCBpbnB1dHM6PGJyPg0KICAgICAgICAgICAgICAgICAgICAgIDxjb2RlIHN0eWxlPSJiYWNrZ3JvdW5kOiAjZjVmNWY1OyBwYWRkaW5nOiA0cHggOHB4OyBib3JkZXItcmFkaXVzOiA0cHg7IGRpc3BsYXk6IGlubGluZS1ibG9jazsgbWFyZ2luLXRvcDogNXB4OyI-R0VUIC9pbnB1dHM8L2NvZGU-DQogICAgICAgICAgICAgICAgICAgIDwvbGk-DQogICAgICAgICAgICAgICAgICAgIDxsaSBzdHlsZT0ibWFyZ2luLWJvdHRvbTogMTBweDsiPlN0YXJ0IHlvdXIgY3Jldzo8YnI-DQogICAgICAgICAgICAgICAgICAgICAgPGNvZGUgc3R5bGU9ImJhY2tncm91bmQ6ICNmNWY1ZjU7IHBhZGRpbmc6IDRweCA4cHg7IGJvcmRlci1yYWRpdXM6IDRweDsgZGlzcGxheTogaW5saW5lLWJsb2NrOyBtYXJnaW4tdG9wOiA1cHg7Ij5QT1NUIC9raWNrb2ZmPC9jb2RlPg0KICAgICAgICAgICAgICAgICAgICA8L2xpPg0KICAgICAgICAgICAgICAgICAgICA8bGkgc3R5bGU9Im1hcmdpbi1ib3R0b206IDEwcHg7Ij5DaGVjayBleGVjdXRpb24gc3RhdHVzOjxicj4NCiAgICAgICAgICAgICAgICAgICAgICA8Y29kZSBzdHlsZT0iYmFja2dyb3VuZDogI2Y1ZjVmNTsgcGFkZGluZzogNHB4IDhweDsgYm9yZGVyLXJhZGl1czogNHB4OyBkaXNwbGF5OiBpbmxpbmUtYmxvY2s7IG1hcmdpbi10b3A6IDVweDsiPkdFVCAvc3RhdHVzL3t0YXNrX2lkfTwvY29kZT4NCiAgICAgICAgICAgICAgICAgICAgPC9saT4NCiAgICAgICAgICAgICAgICAgIDwvb2w-DQogICAgICAgICAgICAgICAgICA8cCBzdHlsZT0ibWFyZ2luOiAxMHB4IDA7Ij5SZW1lbWJlciB0byBpbmNsdWRlIHlvdXIgYmVhcmVyIHRva2VuIGluIHRoZSBhdXRob3JpemF0aW9uIGhlYWRlciBmb3IgYWxsIHJlcXVlc3RzLjwvcD4NCiAgICAgICAgICAgICAgICA8L3RkPg0KICAgICAgICAgICAgICA8L3RyPg0KICAgICAgICAgICAgICA8dHI-DQogICAgICAgICAgICAgICAgPHRkIGFsaWduPSJjZW50ZXIiIHN0eWxlPSJwYWRkaW5nLWJvdHRvbTogMjBweDsiPg0KICAgICAgICAgICAgICAgICAgPHRhYmxlIGNlbGxwYWRkaW5nPSIwIiBjZWxsc3BhY2luZz0iMCIgYm9yZGVyPSIwIj4NCiAgICAgICAgICAgICAgICAgICAgPHRyPg0KICAgICAgICAgICAgICAgICAgICAgIDx0ZA0KICAgICAgICAgICAgICAgICAgICAgICAgYWxpZ249ImNlbnRlciINCiAgICAgICAgICAgICAgICAgICAgICAgIGJnY29sb3I9IiNFQjY2NTgiDQogICAgICAgICAgICAgICAgICAgICAgICBzdHlsZT0iYm9yZGVyLXJhZGl1czogMTJweDsgcGFkZGluZzogMTBweCAyMHB4OyINCiAgICAgICAgICAgICAgICAgICAgICA-DQogICAgICAgICAgICAgICAgICAgICAgICA8YQ0KICAgICAgICAgICAgICAgICAgICAgICAgICBocmVmPSJodHRwczovL2VlYWEzNjFiZDE5OGJiNDcyZjg3MmM0NDczNDZjM2RkLnVzLWVhc3QtMS5yZXNlbmQtbGlua3MuY29tL0NMMC9odHRwczolMkYlMkZhcHAuY3Jld2FpLmNvbSUyRmNyZXdhaV9wbHVzJTJGZGVwbG95bWVudHMlMkYxMDM0ODIvMS8wMTAwMDE5OGFkZWZkNWY1LWIxMWQ5MjQwLTkxNjUtNGVhYi05ZTY4LWJlMjlkZmMwMmQ0NS0wMDAwMDAvNnBpZnM2MGdiWk5vOGU4eS02d3ZFUDlPSnU2a1p6aUY5YjNBWFB1VlhEMD00MTgiDQogICAgICAgICAgICAgICAgICAgICAgICAgIHRhcmdldD0iX2JsYW5rIg0KICAgICAgICAgICAgICAgICAgICAgICAgICBzdHlsZT0iY29sb3I6ICNmZmY7IHRleHQtZGVjb3JhdGlvbjogbm9uZTsiDQogICAgICAgICAgICAgICAgICAgICAgICA-VmlldyBEZXBsb3ltZW50PC9hPg0KICAgICAgICAgICAgICAgICAgICAgIDwvdGQ-DQogICAgICAgICAgICAgICAgICAgIDwvdHI-DQogICAgICAgICAgICAgICAgICA8L3RhYmxlPg0KICAgICAgICAgICAgICAgIDwvdGQ-DQogICAgICAgICAgICAgIDwvdHI-DQogICAgICAgICAgICA8L3RhYmxlPg0KDQogICAgICAgICAgICA8dGFibGUgY2VsbHBhZGRpbmc9IjAiIGNlbGxzcGFjaW5nPSIwIiBib3JkZXI9IjAiIHdpZHRoPSIxMDAlIj4NCiAgICAgICAgICAgICAgPHRyPg0KICAgICAgICAgICAgICAgIDx0ZCBzdHlsZT0iYm9yZGVyLXRvcDogMXB4IHNvbGlkICNFOEU4RTg7IHBhZGRpbmc6IDIwcHggMDsiPg0KICAgICAgICAgICAgICAgICAgPHAgc3R5bGU9Im1hcmdpbjogMDsiPg0KICAgICAgICAgICAgICAgICAgICBGb3IgZGV0YWlsZWQgQVBJIGRvY3VtZW50YXRpb24sIHZpc2l0IDxhIGhyZWY9Imh0dHBzOi8vZWVhYTM2MWJkMTk4YmI0NzJmODcyYzQ0NzM0NmMzZGQudXMtZWFzdC0xLnJlc2VuZC1saW5rcy5jb20vQ0wwL2h0dHBzOiUyRiUyRmhlbHAuY3Jld2FpLmNvbSUyRnVzaW5nLXlvdXItY3Jld3MtYXBpLWluLWNyZXdhaS8xLzAxMDAwMTk4YWRlZmQ1ZjUtYjExZDkyNDAtOTE2NS00ZWFiLTllNjgtYmUyOWRmYzAyZDQ1LTAwMDAwMC96NmcyZnp3akdRXzdlQkpUYnVBV0xEUVd2QUZSTGpqaG05c2x0R09ZTzRJPTQxOCIgc3R5bGU9ImNvbG9yOiAjRUI2NjU4OyB0ZXh0LWRlY29yYXRpb246IG5vbmU7Ij5vdXIgQVBJIGd1aWRlPC9hPi48YnI-PGJyPg0KICAgICAgICAgICAgICAgICAgICBUaGFuayB5b3UsPGJyPg0KICAgICAgICAgICAgICAgICAgICBTdXBwb3J0IFRlYW0NCiAgICAgICAgICAgICAgICAgIDwvcD4NCiAgICAgICAgICAgICAgICA8L3RkPg0KICAgICAgICAgICAgICA8L3RyPg0KICAgICAgICAgICAgPC90YWJsZT4NCiAgICAgICAgICA8L3RkPg0KICAgICAgICA8L3RyPg0KICAgICAgPC90YWJsZT4NCiAgICA8L3RkPg0KICA8L3RyPg0KPC90YWJsZT4NCg0KICA8L2JvZHk-DQo8L2h0bWw-DQo="
          }
        }
      ]
    },
    "sizeEstimate": 11056,
    "historyId": "400221",
    "internalDate": "1755264833000"
  }
}
        ''',
    }

    try:
        GmailNewThreadTrigger().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    # Example Gmail payload for training - using same structure as run()
    inputs = {
        "crewai_trigger_payload": '''
{
  "result": {
    "id": "198adefd9068d7bc",
    "threadId": "198adefd9068d7bc",
    "labelIds": [
      "UNREAD",
      "CATEGORY_UPDATES",
      "INBOX"
    ],
    "snippet": "Deployment Successful! 🎉 Hi lucas, Your crew / flow has been successfully deployed and is now live! Deployment Name: crewai-gmail-new-thread-trigger API URL: https://crewai-gmail-new-thread-trigger-",
    "payload": {
      "partId": "",
      "mimeType": "multipart/alternative",
      "filename": "",
      "headers": [
        {
          "name": "From",
          "value": "donotreply@crewai.com"
        },
        {
          "name": "To",
          "value": "lucas@crewai.com"
        },
        {
          "name": "Subject",
          "value": "Deployment Success"
        },
        {
          "name": "Date",
          "value": "Fri, 15 Aug 2025 13:33:53 +0000"
        }
      ],
      "body": {
        "size": 0
      },
      "parts": [
        {
          "partId": "0",
          "mimeType": "text/plain",
          "filename": "",
          "body": {
            "size": 774,
            "data": "REVQTE9ZTUVOVCBTVUNDRVNTRlVMISDwn46JDQoNCkhpIGx1Y2FzLA0KWW91ciBjcmV3IC8gZmxvdyBoYXMgYmVlbiBzdWNjZXNzZnVsbHkgZGVwbG95ZWQgYW5kIGlzIG5vdyBsaXZlIQ0KDQpEZXBsb3ltZW50IE5hbWU6IGNyZXdhaS1nbWFpbC1uZXctdGhyZWFkLXRyaWdnZXIgQVBJIFVSTDoNCmh0dHBzOi8vY3Jld2FpLWdtYWlsLW5ldy10aHJlYWQtdHJpZ2dlci1hZmRjZWJlYi0yYy1lZmU1ZjU2ZS5jcmV3YWkuY29tIEJlYXJlcg0KVG9rZW46IDIxOGViMjU2YTllMQ0KDQpZb3VyIGNyZXcgaXMgbm93IGF2YWlsYWJsZSBhcyBhbiBBUEkuIEhlcmUncyBob3cgdG8gdXNlIGl0Og0KDQogMS4gR2V0IHJlcXVpcmVkIGlucHV0czoNCiAgICBHRVQgL2lucHV0cw0KIDIuIFN0YXJ0IHlvdXIgY3JldzoNCiAgICBQT1NUIC9raWNrb2ZmDQogMy4gQ2hlY2sgZXhlY3V0aW9uIHN0YXR1czoNCiAgICBHRVQgL3N0YXR1cy97dGFza19pZH0NCg0KUmVtZW1iZXIgdG8gaW5jbHVkZSB5b3VyIGJlYXJlciB0b2tlbiBpbiB0aGUgYXV0aG9yaXphdGlvbiBoZWFkZXIgZm9yIGFsbA0KcmVxdWVzdHMuDQoNClZpZXcgRGVwbG95bWVudCBodHRwczovL2FwcC5jcmV3YWkuY29tL2NyZXdhaV9wbHVzL2RlcGxveW1lbnRzLzEwMzQ4Mg0KDQpGb3IgZGV0YWlsZWQgQVBJIGRvY3VtZW50YXRpb24sIHZpc2l0IG91ciBBUEkgZ3VpZGUNCmh0dHBzOi8vaGVscC5jcmV3YWkuY29tL3VzaW5nLXlvdXItY3Jld3MtYXBpLWluLWNyZXdhaS4NCg0KVGhhbmsgeW91LA0KU3VwcG9ydCBUZWFt"
          }
        }
      ]
    }
  }
}
        ''',
    }
    try:
        GmailNewThreadTrigger().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        GmailNewThreadTrigger().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    # Example Gmail payload for testing - using same structure as run()
    inputs = {
        "crewai_trigger_payload": '''
{
  "result": {
    "id": "198adefd9068d7bc",
    "threadId": "198adefd9068d7bc",
    "labelIds": [
      "UNREAD",
      "CATEGORY_UPDATES",
      "INBOX"
    ],
    "snippet": "Deployment Successful! 🎉 Hi lucas, Your crew / flow has been successfully deployed and is now live! Deployment Name: crewai-gmail-new-thread-trigger API URL: https://crewai-gmail-new-thread-trigger-",
    "payload": {
      "partId": "",
      "mimeType": "multipart/alternative",
      "filename": "",
      "headers": [
        {
          "name": "From",
          "value": "donotreply@crewai.com"
        },
        {
          "name": "To",
          "value": "lucas@crewai.com"
        },
        {
          "name": "Subject",
          "value": "Deployment Success"
        },
        {
          "name": "Date",
          "value": "Fri, 15 Aug 2025 13:33:53 +0000"
        }
      ],
      "body": {
        "size": 0
      },
      "parts": [
        {
          "partId": "0",
          "mimeType": "text/plain",
          "filename": "",
          "body": {
            "size": 774,
            "data": "REVQTE9ZTUVOVCBTVUNDRVNTRlVMISDwn46JDQoNCkhpIGx1Y2FzLA0KWW91ciBjcmV3IC8gZmxvdyBoYXMgYmVlbiBzdWNjZXNzZnVsbHkgZGVwbG95ZWQgYW5kIGlzIG5vdyBsaXZlIQ0KDQpEZXBsb3ltZW50IE5hbWU6IGNyZXdhaS1nbWFpbC1uZXctdGhyZWFkLXRyaWdnZXIgQVBJIFVSTDoNCmh0dHBzOi8vY3Jld2FpLWdtYWlsLW5ldy10aHJlYWQtdHJpZ2dlci1hZmRjZWJlYi0yYy1lZmU1ZjU2ZS5jcmV3YWkuY29tIEJlYXJlcg0KVG9rZW46IDIxOGViMjU2YTllMQ0KDQpZb3VyIGNyZXcgaXMgbm93IGF2YWlsYWJsZSBhcyBhbiBBUEkuIEhlcmUncyBob3cgdG8gdXNlIGl0Og0KDQogMS4gR2V0IHJlcXVpcmVkIGlucHV0czoNCiAgICBHRVQgL2lucHV0cw0KIDIuIFN0YXJ0IHlvdXIgY3JldzoNCiAgICBQT1NUIC9raWNrb2ZmDQogMy4gQ2hlY2sgZXhlY3V0aW9uIHN0YXR1czoNCiAgICBHRVQgL3N0YXR1cy97dGFza19pZH0NCg0KUmVtZW1iZXIgdG8gaW5jbHVkZSB5b3VyIGJlYXJlciB0b2tlbiBpbiB0aGUgYXV0aG9yaXphdGlvbiBoZWFkZXIgZm9yIGFsbA0KcmVxdWVzdHMuDQoNClZpZXcgRGVwbG95bWVudCBodHRwczovL2FwcC5jcmV3YWkuY29tL2NyZXdhaV9wbHVzL2RlcGxveW1lbnRzLzEwMzQ4Mg0KDQpGb3IgZGV0YWlsZWQgQVBJIGRvY3VtZW50YXRpb24sIHZpc2l0IG91ciBBUEkgZ3VpZGUNCmh0dHBzOi8vaGVscC5jcmV3YWkuY29tL3VzaW5nLXlvdXItY3Jld3MtYXBpLWluLWNyZXdhaS4NCg0KVGhhbmsgeW91LA0KU3VwcG9ydCBUZWFt"
          }
        }
      ]
    }
  }
}
        ''',
    }

    try:
        GmailNewThreadTrigger().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

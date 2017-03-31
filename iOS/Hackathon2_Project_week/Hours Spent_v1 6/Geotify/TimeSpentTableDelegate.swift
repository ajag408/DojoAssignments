//
//  TimeSpentTableDelegate.swift
//  Hours Spent
//
//  Created by Akash Jagannathan on 3/27/17.
//  Copyright © 2017 Ryan Munguia. All rights reserved.
//

import UIKit
import CoreLocation
protocol TimeSpentTableDelegate: class{
  func timeSpentTableDelegate(by controller: TimeSpentTable, didPressCancelButton button: UIBarButtonItem)
}

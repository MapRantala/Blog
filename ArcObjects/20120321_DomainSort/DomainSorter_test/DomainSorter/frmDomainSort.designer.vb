'Imports MSFlexGridLib

<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> Partial Class frmDomainSort
#Region "Windows Form Designer generated code "
    <System.Diagnostics.DebuggerNonUserCode()> Public Sub New()
        MyBase.New()
        'This call is required by the Windows Form Designer.
        InitializeComponent()
    End Sub
    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()> Protected Overloads Overrides Sub Dispose(ByVal Disposing As Boolean)
        If Disposing Then
            Static fTerminateCalled As Boolean
            If Not fTerminateCalled Then
                Form_Terminate_Renamed()
                fTerminateCalled = True
            End If
            If Not components Is Nothing Then
                components.Dispose()
            End If
        End If
        MyBase.Dispose(Disposing)
    End Sub
    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer
    Public ToolTip1 As System.Windows.Forms.ToolTip
    Public WithEvents grdDomain As System.Windows.Forms.DataGridView 'MSFlexGridLib.MSFlexGrid 'AxMSFlexGridLib.AxMSFlexGrid
    Public WithEvents cmdCancel As System.Windows.Forms.Button
    Public WithEvents cmdOK As System.Windows.Forms.Button
    Public WithEvents radSortCode As System.Windows.Forms.RadioButton
    Public WithEvents radSortDescription As System.Windows.Forms.RadioButton
    Public WithEvents fraSortItem As System.Windows.Forms.GroupBox
    Public WithEvents radSortDescending As System.Windows.Forms.RadioButton
    Public WithEvents radSortAscending As System.Windows.Forms.RadioButton
    Public WithEvents fraSortType As System.Windows.Forms.GroupBox
    Public WithEvents cmbDomains As System.Windows.Forms.ComboBox
    Public WithEvents _Label1_1 As System.Windows.Forms.Label
    Public WithEvents _Label1_0 As System.Windows.Forms.Label
    '*RANTY Public WithEvents Label1 As Microsoft.VisualBasic.Compatibility.VB6.LabelArray
    '*RANTY Public WithEvents optSortItem As Microsoft.VisualBasic.Compatibility.VB6.RadioButtonArray
    '*RANTY Public WithEvents optSortType As Microsoft.VisualBasic.Compatibility.VB6.RadioButtonArray
    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()> Private Sub InitializeComponent()
        Me.components = New System.ComponentModel.Container
        Me.ToolTip1 = New System.Windows.Forms.ToolTip(Me.components)
        Me.grdDomain = New System.Windows.Forms.DataGridView
        Me.cmdCancel = New System.Windows.Forms.Button
        Me.cmdOK = New System.Windows.Forms.Button
        Me.fraSortItem = New System.Windows.Forms.GroupBox
        Me.radSortCode = New System.Windows.Forms.RadioButton
        Me.radSortDescription = New System.Windows.Forms.RadioButton
        Me.fraSortType = New System.Windows.Forms.GroupBox
        Me.radSortDescending = New System.Windows.Forms.RadioButton
        Me.radSortAscending = New System.Windows.Forms.RadioButton
        Me.cmbDomains = New System.Windows.Forms.ComboBox
        Me._Label1_1 = New System.Windows.Forms.Label
        Me._Label1_0 = New System.Windows.Forms.Label
        CType(Me.grdDomain, System.ComponentModel.ISupportInitialize).BeginInit()
        Me.fraSortItem.SuspendLayout()
        Me.fraSortType.SuspendLayout()
        Me.SuspendLayout()
        '
        'grdDomain
        '
        Me.grdDomain.AllowUserToAddRows = False
        Me.grdDomain.AllowUserToDeleteRows = False
        Me.grdDomain.AllowUserToOrderColumns = True
        Me.grdDomain.Anchor = CType((((System.Windows.Forms.AnchorStyles.Top Or System.Windows.Forms.AnchorStyles.Bottom) _
                    Or System.Windows.Forms.AnchorStyles.Left) _
                    Or System.Windows.Forms.AnchorStyles.Right), System.Windows.Forms.AnchorStyles)
        Me.grdDomain.Location = New System.Drawing.Point(10, 162)
        Me.grdDomain.Name = "grdDomain"
        Me.grdDomain.RowHeadersVisible = False
        Me.grdDomain.Size = New System.Drawing.Size(253, 167)
        Me.grdDomain.TabIndex = 11
        '
        'cmdCancel
        '
        Me.cmdCancel.Anchor = CType((System.Windows.Forms.AnchorStyles.Bottom Or System.Windows.Forms.AnchorStyles.Right), System.Windows.Forms.AnchorStyles)
        Me.cmdCancel.BackColor = System.Drawing.SystemColors.Control
        Me.cmdCancel.Cursor = System.Windows.Forms.Cursors.Default
        Me.cmdCancel.Font = New System.Drawing.Font("Arial", 8.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.cmdCancel.ForeColor = System.Drawing.SystemColors.ControlText
        Me.cmdCancel.Location = New System.Drawing.Point(198, 334)
        Me.cmdCancel.Name = "cmdCancel"
        Me.cmdCancel.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.cmdCancel.Size = New System.Drawing.Size(65, 21)
        Me.cmdCancel.TabIndex = 10
        Me.cmdCancel.Text = "&Cancel"
        Me.cmdCancel.UseVisualStyleBackColor = False
        '
        'cmdOK
        '
        Me.cmdOK.Anchor = CType((System.Windows.Forms.AnchorStyles.Bottom Or System.Windows.Forms.AnchorStyles.Right), System.Windows.Forms.AnchorStyles)
        Me.cmdOK.BackColor = System.Drawing.SystemColors.Control
        Me.cmdOK.Cursor = System.Windows.Forms.Cursors.Default
        Me.cmdOK.Font = New System.Drawing.Font("Arial", 8.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.cmdOK.ForeColor = System.Drawing.SystemColors.ControlText
        Me.cmdOK.Location = New System.Drawing.Point(130, 334)
        Me.cmdOK.Name = "cmdOK"
        Me.cmdOK.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.cmdOK.Size = New System.Drawing.Size(65, 21)
        Me.cmdOK.TabIndex = 9
        Me.cmdOK.Text = "&OK"
        Me.cmdOK.UseVisualStyleBackColor = False
        '
        'fraSortItem
        '
        Me.fraSortItem.Anchor = CType(((System.Windows.Forms.AnchorStyles.Top Or System.Windows.Forms.AnchorStyles.Left) _
                    Or System.Windows.Forms.AnchorStyles.Right), System.Windows.Forms.AnchorStyles)
        Me.fraSortItem.BackColor = System.Drawing.SystemColors.Control
        Me.fraSortItem.Controls.Add(Me.radSortCode)
        Me.fraSortItem.Controls.Add(Me.radSortDescription)
        Me.fraSortItem.Font = New System.Drawing.Font("Arial", 8.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.fraSortItem.ForeColor = System.Drawing.SystemColors.ControlText
        Me.fraSortItem.Location = New System.Drawing.Point(10, 86)
        Me.fraSortItem.Name = "fraSortItem"
        Me.fraSortItem.Padding = New System.Windows.Forms.Padding(0)
        Me.fraSortItem.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.fraSortItem.Size = New System.Drawing.Size(255, 43)
        Me.fraSortItem.TabIndex = 5
        Me.fraSortItem.TabStop = False
        Me.fraSortItem.Text = "Sort Item"
        '
        'radSortCode
        '
        Me.radSortCode.BackColor = System.Drawing.SystemColors.Control
        Me.radSortCode.Cursor = System.Windows.Forms.Cursors.Default
        Me.radSortCode.Font = New System.Drawing.Font("Arial", 8.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.radSortCode.ForeColor = System.Drawing.SystemColors.ControlText
        Me.radSortCode.Location = New System.Drawing.Point(22, 18)
        Me.radSortCode.Name = "radSortCode"
        Me.radSortCode.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.radSortCode.Size = New System.Drawing.Size(87, 15)
        Me.radSortCode.TabIndex = 7
        Me.radSortCode.TabStop = True
        Me.radSortCode.Text = "Code"
        Me.radSortCode.UseVisualStyleBackColor = False
        '
        'radSortDescription
        '
        Me.radSortDescription.BackColor = System.Drawing.SystemColors.Control
        Me.radSortDescription.Cursor = System.Windows.Forms.Cursors.Default
        Me.radSortDescription.Font = New System.Drawing.Font("Arial", 8.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.radSortDescription.ForeColor = System.Drawing.SystemColors.ControlText
        Me.radSortDescription.Location = New System.Drawing.Point(126, 16)
        Me.radSortDescription.Name = "radSortDescription"
        Me.radSortDescription.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.radSortDescription.Size = New System.Drawing.Size(87, 22)
        Me.radSortDescription.TabIndex = 6
        Me.radSortDescription.TabStop = True
        Me.radSortDescription.Text = "Description"
        Me.radSortDescription.UseVisualStyleBackColor = False
        '
        'fraSortType
        '
        Me.fraSortType.Anchor = CType(((System.Windows.Forms.AnchorStyles.Top Or System.Windows.Forms.AnchorStyles.Left) _
                    Or System.Windows.Forms.AnchorStyles.Right), System.Windows.Forms.AnchorStyles)
        Me.fraSortType.BackColor = System.Drawing.SystemColors.Control
        Me.fraSortType.Controls.Add(Me.radSortDescending)
        Me.fraSortType.Controls.Add(Me.radSortAscending)
        Me.fraSortType.Font = New System.Drawing.Font("Arial", 8.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.fraSortType.ForeColor = System.Drawing.SystemColors.ControlText
        Me.fraSortType.Location = New System.Drawing.Point(10, 36)
        Me.fraSortType.Name = "fraSortType"
        Me.fraSortType.Padding = New System.Windows.Forms.Padding(0)
        Me.fraSortType.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.fraSortType.Size = New System.Drawing.Size(255, 43)
        Me.fraSortType.TabIndex = 2
        Me.fraSortType.TabStop = False
        Me.fraSortType.Text = "Sort Type"
        '
        'radSortDescending
        '
        Me.radSortDescending.BackColor = System.Drawing.SystemColors.Control
        Me.radSortDescending.Cursor = System.Windows.Forms.Cursors.Default
        Me.radSortDescending.Font = New System.Drawing.Font("Arial", 8.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.radSortDescending.ForeColor = System.Drawing.SystemColors.ControlText
        Me.radSortDescending.Location = New System.Drawing.Point(126, 18)
        Me.radSortDescending.Name = "radSortDescending"
        Me.radSortDescending.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.radSortDescending.Size = New System.Drawing.Size(87, 22)
        Me.radSortDescending.TabIndex = 4
        Me.radSortDescending.TabStop = True
        Me.radSortDescending.Text = "Descending"
        Me.radSortDescending.UseVisualStyleBackColor = False
        '
        'radSortAscending
        '
        Me.radSortAscending.BackColor = System.Drawing.SystemColors.Control
        Me.radSortAscending.Cursor = System.Windows.Forms.Cursors.Default
        Me.radSortAscending.Font = New System.Drawing.Font("Arial", 8.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.radSortAscending.ForeColor = System.Drawing.SystemColors.ControlText
        Me.radSortAscending.Location = New System.Drawing.Point(22, 18)
        Me.radSortAscending.Name = "radSortAscending"
        Me.radSortAscending.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.radSortAscending.Size = New System.Drawing.Size(87, 22)
        Me.radSortAscending.TabIndex = 3
        Me.radSortAscending.TabStop = True
        Me.radSortAscending.Text = "Ascending"
        Me.radSortAscending.UseVisualStyleBackColor = False
        '
        'cmbDomains
        '
        Me.cmbDomains.Anchor = CType(((System.Windows.Forms.AnchorStyles.Top Or System.Windows.Forms.AnchorStyles.Left) _
                    Or System.Windows.Forms.AnchorStyles.Right), System.Windows.Forms.AnchorStyles)
        Me.cmbDomains.BackColor = System.Drawing.SystemColors.Window
        Me.cmbDomains.Cursor = System.Windows.Forms.Cursors.Default
        Me.cmbDomains.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList
        Me.cmbDomains.Font = New System.Drawing.Font("Arial", 8.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.cmbDomains.ForeColor = System.Drawing.SystemColors.WindowText
        Me.cmbDomains.Location = New System.Drawing.Point(106, 6)
        Me.cmbDomains.Name = "cmbDomains"
        Me.cmbDomains.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.cmbDomains.Size = New System.Drawing.Size(159, 22)
        Me.cmbDomains.Sorted = True
        Me.cmbDomains.TabIndex = 1
        '
        '_Label1_1
        '
        Me._Label1_1.BackColor = System.Drawing.SystemColors.Control
        Me._Label1_1.Cursor = System.Windows.Forms.Cursors.Default
        Me._Label1_1.Font = New System.Drawing.Font("Arial", 8.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me._Label1_1.ForeColor = System.Drawing.SystemColors.ControlText
        Me._Label1_1.Location = New System.Drawing.Point(10, 140)
        Me._Label1_1.Name = "_Label1_1"
        Me._Label1_1.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me._Label1_1.Size = New System.Drawing.Size(91, 15)
        Me._Label1_1.TabIndex = 8
        Me._Label1_1.Text = "Domain after sort:"
        '
        '_Label1_0
        '
        Me._Label1_0.BackColor = System.Drawing.SystemColors.Control
        Me._Label1_0.Cursor = System.Windows.Forms.Cursors.Default
        Me._Label1_0.Font = New System.Drawing.Font("Arial", 8.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me._Label1_0.ForeColor = System.Drawing.SystemColors.ControlText
        Me._Label1_0.Location = New System.Drawing.Point(10, 10)
        Me._Label1_0.Name = "_Label1_0"
        Me._Label1_0.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me._Label1_0.Size = New System.Drawing.Size(91, 15)
        Me._Label1_0.TabIndex = 0
        Me._Label1_0.Text = "Available Domains:"
        '
        'frmDomainSort
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 14.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.BackColor = System.Drawing.SystemColors.Control
        Me.ClientSize = New System.Drawing.Size(271, 361)
        Me.Controls.Add(Me.grdDomain)
        Me.Controls.Add(Me.cmdCancel)
        Me.Controls.Add(Me.cmdOK)
        Me.Controls.Add(Me.fraSortItem)
        Me.Controls.Add(Me.fraSortType)
        Me.Controls.Add(Me.cmbDomains)
        Me.Controls.Add(Me._Label1_1)
        Me.Controls.Add(Me._Label1_0)
        Me.Cursor = System.Windows.Forms.Cursors.Default
        Me.Font = New System.Drawing.Font("Arial", 8.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Location = New System.Drawing.Point(4, 23)
        Me.MaximizeBox = False
        Me.MinimizeBox = False
        Me.Name = "frmDomainSort"
        Me.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.Text = "Domain Sort"
        CType(Me.grdDomain, System.ComponentModel.ISupportInitialize).EndInit()
        Me.fraSortItem.ResumeLayout(False)
        Me.fraSortType.ResumeLayout(False)
        Me.ResumeLayout(False)

    End Sub
#End Region
End Class